##################################################################
# Homework 1.5
#   Task: Имеется группа студентов (характеристики: Имя, Фамилия, Пол,
# опыт в программировании, 5 оценок по 10-бальной системе и оценка за
# экзамен по 10-бальной системе.
#   Необходимые команды:
# 1) Средняя оценка за домашние задания и экзамен по всей группе;
# 2) Средняя оценка по параметрам, которые были выбраны пользователем
# 3) Нахождение лучщих студентов
###################################################################
# Исходные данные
###################################################################
import sys
students = [
        {"Name":"Alex","Surname":"Ivanov","Gender":"M","Experienced":False,
         "Homeworks":[10,5,7,3,6],"Exam":8},
        {"Name":"Liz","Surname":"Ackerman","Gender":"F","Experienced":True,
         "Homeworks":[9,10,10,8,9],"Exam":10},
        {"Name":"Ann","Surname":"Bail","Gender":"F","Experienced":False,
         "Homeworks":[8,5,2,7,4],"Exam":5},
        {"Name":"Nick","Surname":"Baxendale","Gender":"M","Experienced":True,
         "Homeworks":[10,9,10,9,8],"Exam":10},
        {"Name":"Alex","Surname":"Batchler","Gender":"M","Experienced":False,
         "Homeworks":[7,8,6,7,9],"Exam":7},
        {"Name":"Dave","Surname":"Blackmore","Gender":"M","Experienced":True,
         "Homeworks":[5,5,3,7,4],"Exam":5},
        {"Name":"Kate","Surname":"Cordington","Gender":"F","Experienced":False,
         "Homeworks":[3,5,6,4,9],"Exam":7},
        {"Name":"Ann","Surname":"Bail","Gender":"F","Experienced":True,
         "Homeworks":[8,7,8,6,9],"Exam":9},
        {"Name":"Alex","Surname":"Coghill","Gender":"M","Experienced":False,
         "Homeworks":[7,3,5,2,7],"Exam":6},
        {"Name":"Dagon","Surname":"Orzechowski","Gender":"M","Experienced":True,
         "Homeworks":[7,10,5,7,10],"Exam":9}
    ]


###################################################################
# Функция count_avg_by_person - подсчет среднего по отдельному студенту
###################################################################
def count_avg_by_person(student):
        avg_homework = 0
        exam = student["Exam"]
        homework_marks = student["Homeworks"]
        count_marks = 0
        for mark in homework_marks:
            count_marks += 1
            avg_homework += mark
        avg_homework /=count_marks
        return avg_homework, exam

    
###################################################################
# Функция count_statistic - основная функция подсчета статистики по
# всей группе(с выборкой и без)
###################################################################
def count_statistic(students, option):
    avg_group1_homework = 0
    avg_group1_exam = 0
    avg_group2_homework = 0
    avg_group2_exam = 0
    if option == "Gender":
        avg_group1_homework, avg_group1_exam = avg_custom_group(students, option, "M") 
        avg_group2_homework, avg_group2_exam = avg_custom_group(students, option, "F")
        return avg_group1_homework, avg_group1_exam, avg_group2_homework, avg_group2_exam
    elif option == "Experienced":
        avg_group1_homework, avg_group1_exam = avg_custom_group(students, option, True) 
        avg_group2_homework, avg_group2_exam = avg_custom_group(students, option, False)
        return avg_group1_homework, avg_group1_exam, avg_group2_homework, avg_group2_exam
    else:
        avg_group1_homework, avg_group1_exam = avg_custom_group(students, option, None) 
        return avg_group1_homework, avg_group1_exam


###################################################################
# Функция avg_custom_group - подсчет статистики относительно всей
# группы по определенному признаку
###################################################################
def avg_custom_group(students, option, value):
    avg_custom_group_homework = 0
    avg_custom_group_exam = 0
    count_custom_group = 0
    for student in students:        
        if student[option] == value or value == None:
            avg_homework_by_person, avg_exam_by_person = count_avg_by_person(student)
            avg_custom_group_homework += avg_homework_by_person
            avg_custom_group_exam += avg_exam_by_person
            count_custom_group += 1
    avg_custom_group_homework /= count_custom_group
    avg_custom_group_exam /= count_custom_group
    return avg_custom_group_homework, avg_custom_group_exam



###################################################################
# Функция find_best - поиск лучших студентов по всей группе
###################################################################
def find_best(students):
    best_students = []
    all_students = []
    max_points = 0
    for student in students:
        homeworks, exam = count_avg_by_person(student)
        points = 0.6 * homeworks + 0.4 * exam
        if points > max_points:
            max_points = points
        all_students.append(points)
    for index, student_points in enumerate(all_students):
        if student_points == max_points:
            best_students.append(students[index]["Name"] +" "+ students[all_students.index(student_points)]["Surname"])
    print
    return best_students, max_points

###################################################################
# Функция main - работа с пользователем и основная логика программы
###################################################################
def main():


    ###################################################################
    # Функция input_option - подготовка условия выборки
    ###################################################################
    def input_option():
        option = input("Выберите параметр ([П]ол, [О]пыт программирования):")
        if option.upper() == "П":
            print("Средняя оценка за домашние задания у мужчин: {}\nСредняя оценка за экзамен у мужчин: {}\n\n\
Средняя оценка за домашние задания у женщин: {}\nСредняя оценка за экзамен у женщин: {}".format(*count_statistic(students, "Gender")))
        elif option.upper() == "О":
            print("Средняя оценка за домашние задания у студентов с опытом: {}\nСредняя оценка за экзамен у студентов с опытом: {}\n\n\
Средняя оценка за домашние задания у студентов без опыта: {}\nСредняя оценка за экзамен у студентов без опыта: {}".format(*count_statistic(students, "Experienced")))
        else:
            print("Неверная команда. Повторите ввод.")
            input_option()
        
    while True:
        comand = input("Введите команду ([В]се студенты, [П]о признаку, [Л]учшие студенты, [З]акончить):")
        if comand.upper() == "В":
            print("Средняя оценка за домашние задания: {}\nСредняя оценка за экзамен: {}\n".format(*list(count_statistic(students,"Name"))))
        elif comand.upper() == "П":
            input_option()
        elif comand.upper() == "Л": 
            best_ones, max_points = find_best(students)
            if len(best_ones) > 1:
                print("Лучшие студенты: {0}. Максимальный балл: {1}".format(", ".join(best_ones), max_points))
            else:
                print("Лучший студент: {}. Максимальный балл: {}".format(best_ones[0], max_points ))
        elif comand.upper() == "З":
            print("Завершение работы. Нажмите любую клавишу")
            input()
            sys.exit()
        else:
            print("Неверная команда. Повторите ввод.")
            main()

if __name__ == '__main__':
    main()









































