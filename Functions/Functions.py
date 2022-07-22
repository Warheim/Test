from Functions_work import directories, documents


def doc_people(doc_number):
    result = 0
    for ask in documents:
        if doc_number in ask.values():
            result = ask['name']
            return result
    if result == 0:
        return doc_people(input('Неверный номер! Введите номер документа повторно: '))


def doc_shelf(doc_number):
    result = 0
    for key, value in directories.items():
        if doc_number in value:
            result = key
            return f'Номер полки: {result}'
    if result == 0:
        return doc_shelf(input('Неверный номер! Введите номер документа повторно: '))


def doc_list():
    for ask in documents:
        print(f'{ask["type"]} "{ask["number"]}" "{ask["name"]}"')
    return ''


def doc_add(add_shelf, add_type, add_number, add_name):
    if add_shelf in directories.keys():
        documents.append({'type': add_type, 'number': add_number, 'name': add_name})
        for key, value in directories.items():
            if key == add_shelf:
                value.append(add_number)
                return f'Документ {add_number} добавлен.'
    else:
        print('Неверный номер полки!')
        return doc_add(input('Введите номер полки для хранения: '), input('Введите тип документа: '),
                       input('Введите номер документа: '), input('Введите имя владельца документа: '))


def doc_delete(doc_number):
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
        return doc_delete(input('Неверный номер! Введите номер документа повторно: '))


def doc_move():
    def enter_number(doc_number):
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
            return enter_number(input('Неверный номер! Введите номер документа повторно: '))

    def enter_shelf(add_shelf):
        if add_shelf in directories.keys():
            return add_shelf
        else:
            return enter_shelf(input('Неверный номер полки! Введите номер полки повторно: '))

    number = enter_number(input('Введите номер документа: '))
    shelf = enter_shelf(input('Введите номер полки: '))

    for key, value in directories.items():
        if key == shelf:
            value.append(number)
    return f'Документ перемещён.'


def doc_add_shelf(add_shelf):
    if add_shelf not in directories.keys():
        directories[add_shelf] = []
        return f'Полка {add_shelf} создана.'
    else:
        return doc_add_shelf(input('Полка уже существует! Введите номер полки повторно: '))


def program(command=(input('Введите команду: ').lower())):
    if command == 'p':
        return doc_people(input('Введите номер документа: '))
    elif command == 's':
        return doc_shelf(input('Введите номер документа: '))
    elif command == 'l':
        return doc_list()
    elif command == 'a':
        return doc_add(input('Введите номер полки для хранения: '), input('Введите тип документа: ').lower(),
                       input('Введите номер документа: '), input('Введите имя владельца документа: ').capitalize())
    elif command == 'd':
        return doc_delete(input('Введите номер документа: '))
    elif command == 'm':
        return doc_move()
    elif command == 'as':
        return doc_add_shelf(input('Введите номер полки для создания: '))
    else:
        return program(command=(input('Неверная команда! Введите команду повторно: ').lower()))


print(program())
