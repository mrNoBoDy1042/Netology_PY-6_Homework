###########################################################################################################
# Task. Прочитать файлы json, определить их кодировку, вывести топ-10 встречаемых слов в каждом файле
###########################################################################################################

import chardet
import json
import os


def get_json_files():
    """Получаем все json файлы в текущей дирректории"""
    json_files = list(filter(lambda x: x.endswith('.json'), os.listdir(os.path.curdir)))
    return json_files


def get_top_words(file):
    """Получаем топ 10 встречаемых слов"""

    # Получаем список новостей
    news = file['rss']['channel']['items']

    # Проходим по каждой статье в новостях
    top_words = {}
    for item in news:
        words = item['description'].split()

        # Проходим по каждому слову в статье
        for word in words:
            if len(word) > 6:

                # Подсчет повторений слов
                if word in top_words:
                    top_words[word] += 1
                else:
                    top_words[word] = 1

    # Конвертация словаря повторений слов в список кортежей для сортировки
    top_words = list(zip(top_words.keys(), top_words.values()))

    # Сортировка списка по количесву повторений слов
    top_words.sort(key=lambda d: d[1], reverse=True)
    return top_words[:10]


def read_file():
    """Определяем кодировку файла и читаем файл"""
    json_files = get_json_files()
    statistics = {}
    for file in json_files:

        # Определяем кодировку файла, передаем на обработку json
        with open(file, 'rb') as byte_file:
            f = byte_file.read()
            result = chardet.detect(f)

            # Передаем в функцию подсчета статистики обработанный json'ом объект
            statistics[file] = get_top_words(json.loads(f.decode(result['encoding'])))
    return statistics


def main():
    # Получаем топ-10 слов в файлах
    statistics = read_file()

    # Форматированный вывод статистики
    for file in statistics:
        words_list = []
        for word in statistics[file]:
            words_list.append(word[0])
        print('В файле ' + file + ' самые встречаемые слова: ', end='')
        print(*words_list, sep=', ', end='.\n')

main()
