# передача данных из бд во view  и обратно
from model import select_all_table, add_in_teacher, add_in_timetables, add_in_contacts, select_table_where_timetable, select_table_where_teacher
from function import *


def add_data(mode):
    match mode:
        # add teacher
        case '1':
            value = (
                input('Введите ваше ФИО через пробел: '),
                input('Введите номер телефона: '),
                input('Введите адресс: '),
                input('Класный руководитель, какого класса ?: '),
                input('Введите основной предмет: '),
            )
            print(value)
            add_in_teacher(value)
        # add parent
        case '2':
            value = (
                input('Введите ваше ФИО через пробел: '),
                input('Введите номер телефона: '),
                input('Введите профессию(не обязательное поле): '),
                input('Введите адресс: '),
                input('Родитель какого ученика ?(ФИО ученика): '),
                input('Введите класс ученика: '),
                input('Введите пол(м\ж): ')
            )
            print(value)
            add_in_contacts(value)
        # add timetable
        case '3':
            flag = True
            quit = ''
            data = []
            while flag:

                # get value class number
                for i, v in enumerate(get_all_classes()):
                    print(f'{i+1}){v} ', end=' ')

                c = input(f'\nВведите номер класса(от 1 до {len(get_all_classes())}): ')
                class_num = get_select_classes(int(c)-1)

                # get value time lesson
                for i, v in enumerate(get_all_time_lesson()):
                    print(f'{i + 1}){v} ', end=' ')

                c = input('Введите время урока: ')
                time = get_select_time_lesson(int(c)-1)

                # get value lesson number
                num_lesson = int(input('Введите номер урока(1-7): '))
                get_select_lesson(num_lesson)

                # get value lesson day
                for i, v in get_all_day().items():
                    print(f'{i}){v}', end=' ')

                c = input('\nВведите день недели(1-6): ')
                weekday = get_select_day(c)

                # get value classroom number
                print('Доступные кабинеты в школе')
                for i in get_all_classroom():
                    print(i, end=' ')

                c = input('Введите номер кабинета: ')
                classroom = get_select_classroom(int(c)-1)

                # get value techer
                c = select_all_table('teachers')
                for i, v in enumerate(c):
                    print(f'id:{v[0]}) учитель {v[1]}')

                f = input('Введите учителя(не обязательное поле)(id): ')
                val = select_table_where_teacher(int(f))
                teacher = val[0][1]

                # get value subject
                for i, v in enumerate(get_all_subject()):
                    print(f'{i+1}) {v}')

                c = input('Введите предмет: ')
                subject = get_select_subject(int(c)-1)

                value = (class_num, num_lesson, time, weekday, classroom, teacher, subject)

                data.append(value)

                quit = input('Желаете еще внести запись в расписание?(y/n): ')

                if quit == 'n':
                    flag = False
            print(f'Всего записей добавлено {len(data)}')
            for i, v in enumerate(data):
                add_in_timetables(v)
                print(f"{i+1}) ", end='')
                print(*v)


def print_data(mode):
    match mode:
        case '1':
            for i, v in enumerate(get_all_classes()):
                print(f'{i + 1}){v} ', end=' ')

            c = input(f'\nВведите номер класса(от 1 до {len(get_all_classes())}): ')

            for i, v in get_all_day().items():
                print(f'{i}){v}', end=' ')

            x = input('\nВведите день недели(1-6): ')
            weekday = get_select_day(x)
            class_num = get_select_classes(int(c)-1)

            val = (class_num, '')
            data = select_table_where_timetable(val)

            print(f'\n-------------------=Расписание для {class_num} на {weekday}=-------------------')

            for i, v in enumerate(data):
                if v[4] == weekday and v[1] == class_num:
                    print(f'\n{v[2]}) {v[7]} | {v[3]} | кабинет:№{v[5]} | препод: {v[6]}')

        case '2':
            data = select_all_table('teachers')
            for i, v in enumerate(data):
                print(f'{i+1}) Учитель {v[5]} | {v[1]} | класный руководитель {v[4]} | телефон: {v[2]} | адрес: {v[3]}')
        case '3':
            data = select_all_table('contacts')
            for i, v in enumerate(data):
                print(f'{i+1}) {v[1]} | родитель ученика: {v[5]} |  класс ученика: {v[6]} | телефон: {v[2]} | адрес: {v[4]} |пол: {v[7]}')
