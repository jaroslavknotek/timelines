import typing


class Note(typing.NamedTuple):
    name: str
    text: str


def to_entity(note: Note):
    return {"PartitionKey": "Note", "RowKey": note.name, "text": note.text}


def from_entity(entity) -> Note:
    return Note(name=entity["RowKey"], text=entity["text"])
