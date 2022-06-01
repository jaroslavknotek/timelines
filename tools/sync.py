import os
import sys

sys.path.append("..")
sys.path.append("../azure_functions")

import json

import azure_functions.shared_code.notes_table_client as ntc
from azure_functions.shared_code.note_model import Note


def _read_file(filepath):
    with open(filepath, "r") as f:
        return f.read()


def _trim_note(note_text, tag):
    header_end = note_text[3:].index("---")
    text = note_text[header_end + 6 :]
    return text.replace(tag, "").strip()


def _trim_name(note_name: str) -> str:
    return note_name.rstrip(".md")


def _get_tagged_notes(notes_root, tag="#show_me"):

    notes_filename = [
        filename for filename in os.listdir(notes_root) if filename.endswith(".md")
    ]
    notes_texts = (
        _read_file(os.path.join(notes_root, note_filename))
        for note_filename in notes_filename
    )

    shownotes = (
        (_trim_name(name), _trim_note(note, tag))
        for name, note in zip(notes_filename, notes_texts)
        if tag in note
    )

    return [Note(name=name, text=text) for name, text in shownotes]


def sync(notes_root: str, wipe: bool = False):
    notes = _get_tagged_notes(notes_root)

    print("loaded", len(notes))
    with open("../azure_functions/local.settings.json", "r") as f:
        keys = json.load(f)["Values"]
        connection_string = keys["StorageAccountConnectionString"]

    client = ntc.NotesClient(connection_string)
    if wipe:
        print("wiping all")
        client.remove_all()
    print("upserting notes")
    client.upsert_notes(notes)
    print("sync done")


if __name__ == "__main__":
    sync(sys.argv[1])
