################################################################################
# Task. Изменить ширину фотографий из папки source обращением к convert.exe
# Разбить выполнение на 4 параллельных процесса
################################################################################
import os
import subprocess
from multiprocessing.dummy import Pool as ThreadPool


################################################################################
# Получение текущего пути, создание необходимой папки, составление списка
# фотографий для обработки
################################################################################
def prepare_to_convert():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Путь до фотографий в папке Source
    path_to_files = os.path.join(current_dir, 'Source')
    os.chdir(path_to_files)
    # Получение списка фотографий
    photo_list = os.listdir()
    # Создаем папку для обработанных фотографий
    try:
        os.mkdir(os.path.join(current_dir, 'Result'))
    # Если возникает ошибка, значит папка уже есть
    except FileExistsError:
        pass
    return current_dir, photo_list


################################################################################
# Обработка фотографий в многопоточном режиме
################################################################################
def main(path, photo_list):
    os.chdir(path)

    ####################################################################################
    # Процедура обработки одной фотографии
    ####################################################################################
    def convert(photo_to_convert):
        # 0 - исходная фотография
        # 1 - обработанная фотография
        subprocess.call('convert.exe {0} -resize 200 {1}'\
                        .format(os.path.join('Source', photo_to_convert), os.path.join('Result', photo_to_convert)))
    # создаем пул на 4 "воркера" для распределения задач
    pool = ThreadPool(4)
    # применяем процедуру convert для каждой фотографии в списке и распределяем выполнение в пуле
    pool.map(convert, photo_list)

if __name__ == '__main__':
    # запускаем выполнение необходимых процедур
    main(*prepare_to_convert())
