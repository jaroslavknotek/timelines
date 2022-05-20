import azure_functions.shared_code.notes_table_client as ntc


def _get_note_html(note):
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


def get_notes_timeline(connection_string):
    client = ntc.NotesClient(connection_string)
    notes = client.read_all()
    return _get_all_html(notes)
