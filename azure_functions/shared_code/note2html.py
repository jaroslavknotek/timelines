import time
from collections import deque

import numpy as np
import shared_code.notes_table_client as ntc
from shared_code.note_model import Note

np.random.seed(seed=4567)


def _get_note_html(note: Note) -> str:
    return f"""
<div class=item>
    <h3>{note.name}</h3>
    <div class=text>
    {note.text}
    </div>
</div>
"""


def _get_all_html(notes) -> str:
    items_html = "".join([_get_note_html(note) for note in notes])

    css = """
.item  {border-style: solid; margin:10px; padding:5px}
.item .text { width = 70%; float=right;}
.item img { float=left; width:25%;}
"""

    return f"""
<html lang="en">
<style>    
{css}
</style>
<body>
{items_html}
</body>
</html>
"""


def _shuffle(arr, idx_a, idx_b):
    tmp = arr[idx_b]
    arr[idx_b] = arr[idx_a]
    arr[idx_a] = tmp


def _roll_by_secs(arr, secs=30 * 60):
    start_time = int(time.time())
    roll_secs = start_time // secs
    return np.roll(arr, roll_secs)


def _shuffle_notes(notes):
    """
    This function makes sure that the notes won't be in the alpabetic order
    and they will roll every 30 minutes. It expects that the number of
    notes will change which shouldn't break the orders. That's why the
    permutation is done in this ineffective way.

    :param notes: Notes in alpha order
    :return: Notes shuffled and rolled
    """

    idxs = [np.random.randint(i + 1) for i in range(len(notes))]
    idxs = _roll_by_secs(idxs)
    notes_copy = list(notes)
    for i, s_idx in enumerate(idxs):
        _shuffle(notes_copy, i, s_idx)
    return notes_copy


def get_notes_timeline(connection_string):
    client = ntc.NotesClient(connection_string)
    notes = client.read_all()
    notes_shuffled = _shuffle_notes(notes)

    return _get_all_html(notes_shuffled)
