import text
from datetime import datetime


def main_menu():
    for i, item in enumerate(text.menu_items):
        print(f'\t{i}. {item}' if i else item)
    while True:
        user_choice = input(text.menu_choice)
        if user_choice.isdigit() and 0 < int(user_choice) < len(text.menu_items):
            return int(user_choice)
        print(text.menu_choice_error)


def show_notes(dict_note: dict, error_message: str):
    if dict_note:
        print()
        for note_id, note in dict_note.items():
            note_list = []
            for item in note.values():
                note_list.append(item)
            print(f'#{note_id} | {note_list[-1]}\nТема: {note_list[0]}\n{note_list[1]}\n')
    else:
        show_message(error_message)


def show_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def input_note(message: list[str]) -> dict[str, str]:
    timestamp = datetime.now().strftime("%d/%m/%y %I:%M")
    data = [input(item) for item in message]
    return {'title': data[0], 'note': data[1], 'timestamp': timestamp}


def input_data(message: str) -> str:
    return input(message)