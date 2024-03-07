menu_items = [
    'Главное меню:',
    'Открыть файл',
    'Сохранить файл',
    'Показать все заметки',
    'Добавить заметку',
    'Показать по дате',
    'Редактировать заметку',
    'Удалить заметку',
    'Выход'
]
menu_choice = 'Выберите пункт меню: '
menu_choice_error = f'Введите пункт меню от 1 до {len(menu_items) - 1}'

load_successful = 'Файл открыт успешно!'
save_successful = 'Файл сохранен успешно!'

empty_dict_note = 'Заметок нет или файл не открыт!'

create_note = ['Введите заголовок заметки: ',
               'Введите заметку: ']

or_enter = ' или ENTER (оставить без изменений): '
edit_note = ['Введите измененный заголовок заметки' + or_enter,
             'Измените заметку' + or_enter]

input_find_date = 'Введите дату для поиска в формате DD/MM/YY: '

input_note_id = 'Введите ID заметки, которую хотите отредактировать: '
delete_note_id = 'Введите ID заметки, которую хотите удалить: '


def error_id_note(note_id: str) -> str:
    return f'Заметки с ID {note_id} не существует!'


def add_note_successful(title: str) -> str:
    return f'Заметка "{title}" создана успешно!'


def edit_note_successful(title: str) -> str:
    return f'Заметка "{title}" изменена успешно!'


def delete_note_successful(title: str) -> str:
    return f'Заметка "{title}" удалена успешно!'


def find_by_date_error(date: str) -> str:
    return f'Заметок созданных {date} не найдено!'
