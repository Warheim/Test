from Functions_work import directories, documents


def doc_people(doc_number: str):
    result = 0
    for ask in documents:
        if doc_number in ask.values():
            result = ask['name']
            return result
    if result == 0:
        return 'Неверный номер!'


def doc_shelf(doc_number: str):
    result = 0
    for key, value in directories.items():
        if doc_number in value:
            result = key
            return f'Номер полки: {result}'
    if result == 0:
        return 'Неверный номер!'


def doc_list():
    for ask in documents:
        return f'{ask["type"]} "{ask["number"]}" "{ask["name"]}"'


def doc_add(add_shelf: str, add_type: str, add_number: str, add_name: str):
    if add_shelf in directories.keys():
        documents.append({'type': add_type, 'number': add_number, 'name': add_name})
        for key, value in directories.items():
            if key == add_shelf:
                value.append(add_number)
                return f'Документ {add_number} добавлен.'
    else:
        return 'Неверный номер!'


def doc_delete(doc_number: str):
    control = []
    for ask in directories.values():
        for look in ask:
            if look == doc_number:
                control.append(look)
                ask.remove(look)
    for task in documents:
        if task['number'] == doc_number:
            documents.remove(task)
            return f'Документ {doc_number} удалён.'
    if len(control) == 0:
        return 'Неверный номер!'


def doc_move():
    def enter_number(doc_number: str):
        temp = []
        for ask in directories.values():
            for task in ask:
                temp.append(task)
        if doc_number in temp:
            for ask in directories.values():
                for task in ask:
                    if task == doc_number:
                        result = doc_number
                        ask.remove(task)
                        return result
        else:
            return 'Неверный номер!'

    def enter_shelf(add_shelf: str):
        if add_shelf in directories.keys():
            return add_shelf
        else:
            return 'Неверный номер!'

    number = enter_number(input('Введите номер документа: '))
    shelf = enter_shelf(input('Введите номер полки: '))

    for key, value in directories.items():
        if key == shelf:
            value.append(number)
    return f'Документ перемещён.'


def doc_add_shelf(add_shelf: str):
    if add_shelf not in directories.keys():
        directories[add_shelf] = []
        return f'Полка {add_shelf} создана.'
    else:
        return 'Неверный номер!'




