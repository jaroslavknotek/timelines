import re
import time
from collections import deque

import mistune
import numpy as np
import shared_code.notes_table_client as ntc
from shared_code.note_model import Note

np.random.seed(seed=4567)


def _handle_latex(note_markdown):
    placeholder_template = "mathplaceholder{}x{}"

    multi_line_matches = re.findall("([$]{3}[^$]*[$]{3})", note_markdown)

    for i, mtch in enumerate(multi_line_matches):
        note_markdown = note_markdown.replace(
            mtch, placeholder_template.format("ml", i)
        )

    single_line_matches = re.findall("([$][^$]*[$])", note_markdown)

    for i, mtch in enumerate(single_line_matches):
        note_markdown = note_markdown.replace(
            mtch, placeholder_template.format("sl", i)
        )

    note_html = mistune.html(note_markdown)

    for i, mtch in enumerate(multi_line_matches):
        match_html_adjusted = f"\\[{mtch.strip('$')}\\]"
        note_html = note_html.replace(
            placeholder_template.format("ml", i), match_html_adjusted
        )

    for i, mtch in enumerate(single_line_matches):
        match_html_adjusted = f"\\({mtch.strip('$')}\\)"
        note_html = note_html.replace(
            placeholder_template.format("sl", i), match_html_adjusted
        )

    return note_html


def _get_note_html(note: Note) -> str:
    note_html = _handle_latex(note.text)

    return f"""
<div class=item>
    <h3>{note.name}</h3>
    <div class=text>
    {note_html}
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
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
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


def get_notes_timeline(connection_string, limit=100):
    client = ntc.NotesClient(connection_string)
    notes = client.read_all()
    notes_shuffled = _shuffle_notes(notes)
    notes_lmtd = notes_shuffled[:limit]

    return _get_all_html(notes_lmtd)
