from datetime import datetime
import json
import os

dict_note = {}
path = 'notes.json'


def open_file():
    global dict_note
    if os.path.exists(path):
        with open(path, 'r', encoding='UTF-8') as json_file:
            dict_note = json.load(json_file)


def save_file():
    global dict_note
    with open(path, 'w', encoding='UTF-8') as json_file:
        json.dump(dict_note, json_file, indent=4, ensure_ascii=False)


def _next_id():
    global dict_note
    return max(map(int, dict_note)) + 1


def add_note(note: dict):
    global dict_note
    if dict_note:
        dict_note[_next_id()] = note
    else:
        dict_note[1] = note


def find_note_by_date(data_date: str) -> dict:
    global dict_note
    result = {}
    current_date = '/'.join([item.zfill(2) for item in data_date.split('/')])
    for note_id, note in dict_note.items():
        if current_date == note['timestamp'].split()[0]:
            result[note_id] = note
    return result


def edit_note(note_id: str, note: dict) -> str:
    global dict_note
    current_note = dict_note[note_id]
    for key in ['title', 'note']:
        current_note[key] = note[key] if note[key] else current_note[key]
    dict_note[note_id] = current_note
    return current_note['title']


def delete_note(note_id: str) -> str:
    global dict_note
    return dict_note.pop(note_id)['title']
