import hashlib
import itertools
import os
import re
from pathlib import Path

import frontmatter
import genanki
import markdown
import typer
from bs4 import BeautifulSoup, Comment
from bs4.element import Tag
from genanki.deck import Deck
from genanki.model import Model

from markdown_anki_decks.sync import sync_deck, sync_model
from markdown_anki_decks.utils import print_success

app = typer.Typer()


def version_callback(value: bool):
    from . import __version__

    if value:
        typer.echo(f"Markdown Anki Decks: {__version__}")
        raise typer.Exit()


@app.command("convert")
def convertMarkdown(
    input_dir: Path = typer.Argument(
        ...,
        help="The input directory. Contains markdown files which will be converted to anki decks.",
    ),
    output_dir: Path = typer.Argument(
        ..., help="The output directory. Anki .apkg files will be written here."
    ),
    sync: bool = typer.Option(
        False,
        "--sync",
        help="Whether or not to synchronize the output with anki using anki connect.",
    ),
    deck_title_prefix: str = typer.Option(
        "",
        "--prefix",
        help="Can be used to make your markdown decks part of a single subdeck. Anki uses `::` to indicate sub decks. `markdown-decks::` could be used to make all generated decks part of a single root deck `markdown-decks`",
    ),
    delete_cards: bool = typer.Option(
        False,
        "--delete",
        help="Whether to delete cards from anki during sync. If sync is false this has no effect.",
    ),
    cloze: bool = typer.Option(
        False,
        "--cloze",
        help="Whether to support cloze syntax",
    ),
    version: bool = typer.Option(
        False, "--version", callback=version_callback, help="Show version information"
    ),
):

    # iterate over the source directory
    for root, _, files in os.walk(input_dir):
        for file in files:
            if is_markdown_file(file):
                deck = parse_markdown(
                    os.path.join(root, file), deck_title_prefix, cloze
                )
                package = genanki.Package(deck)
                # add all image files to the package
                package.media_files = image_files(input_dir)
                path_to_pkg_file = os.path.join(output_dir, f"{Path(file).stem}.apkg")
                package.write_to_file(path_to_pkg_file)
                print_success(f"Created apkg for deck {deck.name}")
                if sync:
                    sync_deck(deck, Path(path_to_pkg_file), delete_cards)
                    for model in deck.models.values():
                        sync_model(model)


ANKI_CLOZE_REGEXP = re.compile(r"{{c\d+::[\s\S]+?}}")


def has_clozes(text):
    """Checks whether text actually has cloze deletions."""
    return bool(ANKI_CLOZE_REGEXP.search(text))


# check if a tag is a question
def is_question_tag(tag: Tag):
    return tag.name == "h2" or (isinstance(tag, Tag) and tag.has_attr("data-question"))


def parse_markdown(
    file: str, deck_title_prefix: str, generate_cloze_model: bool
) -> Deck:
    metadata, markdown_string = frontmatter.parse(read_file(file))
    html = markdown.markdown(
        markdown_string,
        extensions=["fenced_code", "sane_lists", "tables", "codehilite", "md_in_html"],
    )

    soup = BeautifulSoup(html, "html.parser")

    # strip all comments from the html
    comments = soup.findAll(text=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    # get the deck title
    deck_title = Path(file).stem
    h1 = soup.h1
    if h1 is not None and h1.text:
        deck_title = h1.text
    deck_title = deck_title_prefix + deck_title

    # model for an anki deck
    model = genanki.Model(
        model_id=integer_hash(f"{deck_title} model"),
        name=f"{deck_title} model",
        fields=[{"name": "Question"}, {"name": "Answer"}, {"name": "Guid"}],
        templates=[
            {
                "name": "Card 1",
                "qfmt": '<div class="card"><div class="question">{{Question}}</div></div>',
                "afmt": '<div class="card"><div class="question">{{Question}}</div><hr><div class="answer">{{Answer}}</div></div>',
            },
        ],
        css=read_css(file, metadata),
        model_type=Model.FRONT_BACK,
    )

    # model for an anki deck
    cloze_model = genanki.Model(
        model_id=integer_hash(f"{deck_title} cloze model"),
        name=f"{deck_title} cloze model",
        fields=[{"name": "Question"}, {"name": "Answer"}, {"name": "Guid"}],
        templates=[
            {
                "name": "Card 1",
                "qfmt": '<div class="card"><div class="question">{{cloze:Question}}</div></div>',
                "afmt": '<div class="card"><div class="question">{{cloze:Question}}</div><hr><div class="answer">{{Answer}}</div></div>',
            },
        ],
        css=read_css(file, metadata),
        model_type=Model.CLOZE,
    )

    # create the deck
    deck_id = integer_hash(deck_title)
    deck = genanki.Deck(deck_id=deck_id, name=deck_title)

    # add model to deeck
    deck.add_model(model)
    if generate_cloze_model:
        deck.add_model(cloze_model)

    # get the notes
    note_headers = soup.find_all(is_question_tag, recursive=False)
    for header in note_headers:
        # the question is the header
        question = header

        # the contents are everything until the next header
        contents = list(
            itertools.takewhile(
                lambda el: not is_question_tag(el), header.next_siblings
            )
        )

        # wrap the contents in a section tag. the section is the answer.
        answer = soup.new_tag("section")
        if len(contents) > 0:
            contents[0].wrap(answer)
            for content in contents[1:]:
                answer.append(content)

        # create the note using the simple model
        note = FrontIdentifierNote(
            guid=genanki.guid_for(soup_to_html_string(question), deck_id),
            model=(
                cloze_model
                if generate_cloze_model
                and has_clozes(soup_to_plaintext_string(question))
                else model
            ),
            fields=[soup_to_plain_html_string(question), soup_to_plain_html_string(answer)],
        )
        deck.add_note(note)

    return deck


# genanki Note which has a unique id based on the deck and the question
# also has a field for the guid so the guid can be accessed in queries
class FrontIdentifierNote(genanki.Note):
    def __init__(self, guid, model=None, fields=None, sort_field=None, tags=None):
        if fields is not None:
            fields.append(guid)
        super().__init__(
            model=model, fields=fields, sort_field=sort_field, tags=tags, guid=guid
        )


# convert beautiful soup object to a pretty html string
def soup_to_html_string(soup):
    return soup.prettify(formatter="html5")

# convert beautiful soup object to a non-pretty html string
def soup_to_plain_html_string(soup):
    return str(soup)

def soup_to_plaintext_string(soup):
    return soup.get_text()


# convert a file to a string
def read_file(file):
    with open(file, "r", encoding="utf-8") as f:
        markdown_string = f.read()
    return markdown_string


# check if a file is a markdown file
def is_markdown_file(file):
    # TODO(lukemurray): parameterize markdown extensions?
    return file.endswith(".md")


# convert a string into a random integer from 0 to 1<<31 exclusive
# used to create model and deck ids
# from https://stackoverflow.com/a/42089311/11499360
def integer_hash(s: str):
    return int(hashlib.sha256(s.encode("utf-8")).hexdigest(), 16) % (1 << 31)


# get all the image files in a directory
def image_files(source: Path):
    return list(
        str(p)
        for p in itertools.chain(
            source.rglob("*.jpg"),
            source.rglob("*.jpeg"),
            source.rglob("*.png"),
            source.rglob("*.gif"),
        )
    )


def read_css(file: str, metadata: dict) -> str:
    # merge the css files
    markdown_css = Path(__file__).parent / "./styles/markdown.css"
    pygments_css = Path(__file__).parent / "./styles/pygments.css"
    pygments_dark_css = Path(__file__).parent / "./styles/pygments-dark.css"
    custom_css_contents = []
    if "css" in metadata:
        custom_css_paths = metadata["css"]
        if not isinstance(custom_css_paths, list):
            custom_css_paths = [custom_css_paths]
        for custom_css_path in custom_css_paths:
            custom_css_contents.append(
                (Path(file).parent / custom_css_path).read_text("utf-8")
            )

    custom_css = "\n".join(custom_css_contents)

    return f'{markdown_css.read_text("utf-8")}\n{pygments_css.read_text("utf-8")}\n{pygments_dark_css.read_text("utf-8")}\n{custom_css}'


def main():
    app()
