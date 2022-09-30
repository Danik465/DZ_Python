def get_all_time_lesson():
    time = ['8:30 - 9:15', '9:30 - 10:15', '10:30 - 11:15', '11:30 - 12:15', '12:30 - 13:15', '13:25 - 14:10', '13:25 - 15:10']
    return time


def get_select_time_lesson(select):
    time = ['8:30 - 9:15', '9:30 - 10:15', '10:30 - 11:15', '11:30 - 12:15', '12:30 - 13:15', '13:25 - 14:10',
            '13:25 - 15:10']
    return time[select]


def get_all_classes():
    classes = ['1А', '1Б', '2А', '2Б', '3А', '3Б', '5А', '6А', '6Б', '7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '10Б', '11А', '11Б', ]
    return classes


def get_select_classes(select):
    classes = ['1А', '1Б', '2А', '2Б', '3А', '3Б', '5А', '6А', '6Б', '7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '10Б', '11А', '11Б', ]
    return classes[select]


def get_all_subject():
    subj = ['Математика', 'Физика', 'Русский язык', 'Английский язык', 'Информатика', 'Биология', 'ИЗО', 'ОБЖ', 'Геометрия', 'Астрономия', 'Алгебра', 'Литература', 'Музыка', 'Физ-ра', 'Труд']
    return subj


def get_select_subject(select):
    subj = ['Математика', 'Физика', 'Русский язык', 'Английский язык', 'Информатика', 'Биология', 'ИЗО', 'ОБЖ',
            'Геометрия', 'Астрономия', 'Алгебра', 'Литература', 'Музыка', 'Физ-ра', 'Труд']
    return subj[select]


def get_all_classroom():
    classroom = [str(i) for i in range(1, 41)]
    return classroom


def get_select_classroom(select):
    classroom = [str(i) for i in range(1, 41)]
    return classroom[select]


def get_select_lesson(select):
    flag = True
    while flag:
        if select < 8:
            return str([i for i in range(1, 8)][select])
        else:
            print('Вы ввели некоректный день, повторите пожалуйста')
            select = int(input('Введите номер урока(1-7): '))


def get_select_day(select):
    day = {'1': 'Понедельник', '2': 'Вторник', '3': 'Среда',  '4': 'Четверг',  '5': 'Пятница',  '6': 'Суббота', }
    return day[select]


def get_all_day():
    day = {'1': 'Понедельник', '2': 'Вторник', '3': 'Среда',  '4': 'Четверг',  '5': 'Пятница',  '6': 'Суббота', }
    return day

