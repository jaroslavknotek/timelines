import sys
import os

sys.path.append("..")
sys.path.append("../azure_functions")

import json
import azure_functions.shared_code.notes_table_client as ntc
from azure_functions.shared_code.note_model import Note

def _read_note(filename:str, notes_root:str) ->Note:
    filepath = os.path.join(notes_root,filename)
    with open(filepath) as f:
        text_all = f.read()
        # skipping the first `---` to find the second occurence
        header_end = text_all[3:].index('---')
        text = text_all[header_end + 6:]
        text = text.replace("#show_me","").strip()
        name = filename[:-3]
        return Note(name = name, text= text)

def _get_notes(path_to_filelist:str, notes_root:str):
    with open(path_to_filelist,'r') as f:
        filenames = f.readlines()
    
    return [_read_note(filename.strip(), notes_root) for filename in filenames]
    

def sync(path_to_filelist:str, notes_root:str):
    notes = _get_notes(path_to_filelist, notes_root)
    
    with open("../azure_functions/local.settings.json", "r") as f:
        keys = json.load(f)["Values"]
        connection_string = keys["StorageAccountConnectionString"]
        
    client = ntc.NotesClient(connection_string)
    client.upsert_notes(notes)

if __name__ == "__main__":
    sync(sys.argv[1], sys.argv[2])
    
