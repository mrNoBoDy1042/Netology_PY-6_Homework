##################################################################################
# Homework 2.4 Task
#
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C
#################################################################################
# Пример на настоящих данных
#
# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1
#################################################################################
# не забываем организовывать собственный код в функции
#################################################################################
import os


#################################################################################
# Находим папку Migrations и получаем список файлов
#################################################################################
def find_all_files():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_files = os.path.join(current_dir, 'migrations')
    os.chdir(path_to_files)
    sql_files = list(filter(lambda x: x.endswith('.sql'), os.listdir()))
    return sql_files


#################################################################################
# Получаем строку для поиска
#################################################################################
def get_string():
    return input('Введите строку для поиска:')


################################################################################
# Ищем все файлы с данной строкой
################################################################################
def find_matching_files(files_list):

    #################################################################################
    # Работа с файлом. Чтение и поиск строки
    #################################################################################
    def find_string(user_file, user_string):

        #################################################################################
        # Чтение файла
        #################################################################################
        def read_file(file):
            with open(file) as f:

                # чтение файла
                try:
                    return f.read()
                # если не удается прочитать файл - обработка ошибки
                except UnicodeDecodeError:
                    pass

        # Получаем содержимое файла, если его невозможно прочитать - возвращается None
        file_content = read_file(user_file)
        if file_content is not None:

            # Если в файле есть данная строка - возвращаем имя файла
            if user_string.lower() in file_content.lower():
                return user_file

    ################################################################################
    # Вывод найденных файлов на печать
    ################################################################################
    def print_result(found_files):
        print()
        for item in found_files:
            print(item)
        print('\nДля завершения поиска - CTRL + C')
        print('-'*50, end='\n\n')

    # Получаем строку пользователя и ищем ее в файлах
    user_input = get_string()
    suitable_files = []
    for file in files_list:
        result = find_string(file, user_input)

        # Если процедура поиска вернула имя файла - добавляем в список совпадений
        if result is not None:
            suitable_files.append(result)

    # Печать найденных результатов
    print_result(suitable_files)
    # Продолжение поиска среди найденных файлов
    find_matching_files(suitable_files)


if __name__ == '__main__':
    # Получение списка файлов
    list_files = find_all_files()
    # Инициализация поиска среди файлов
    find_matching_files(list_files)
