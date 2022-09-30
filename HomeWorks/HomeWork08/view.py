# отображение данных  прием данных от пользователя
from controller import add_data, print_data


def mode(select_mode):
    mode_sel = 'unknown'
    if select_mode == '1':

        print('Какцю запись вы желаете внести в базу ? ')
        print('1) Добавить учителя\n2) Добавить родителя\n3) Добавить урок в расписание\n')

        add_db = input('Введите номер программы')
        add_data(add_db)

    elif select_mode == '2':
        print('Какцю запись вы желаете изменить в базе ? ')
        print('1) Изменить данные учителя\n2) Изменить данные контакта\n3) Изменить урок в расписании\n')

        update_db = input('Введите номер программы')
        mode_sel = update_db
        match update_db:
            case '1':
                print('1')
            case '2':
                print('2')
            case '3':
                print('3')

    elif select_mode == '3':
        print('Какцю информацию желаете получить ? ')
        print('1) Расписание\n2) Данные учителя\n3) Данные контактов\n')

        info = input('Введите номер программы')
        print_data(info)
    else:
        print(f'Данных по запросу {select_mode, mode_sel} нет, попробуете повторить действия и выбрать правильную программу.')


def menu():
    print('Добро пожаловать в интерактивную среду управления Школой №111')
    print('\nВозможности системы:\n1) Внести запись в базу\n2) Изменить данные в базе\n3) Получить информацию\n')
    flag = True
    status = 'activ'
    while flag:

        select = input('Выбирите действие: ')
        mode(select)

        status = input('Желаете продолжить ? y/n')
        if status == 'n':
            print('\nБлагодарим за использование нашей системы.\nВсего доброго!')
            flag = False
        else:
            print('\nВозможности системы:\n1) Внести запись в базу\n2) Изменить данные в базе\n3) Получить информацию\n')


def main():
    menu()
