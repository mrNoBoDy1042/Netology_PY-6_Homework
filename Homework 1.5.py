##################################################################
# Homework 1.5
#   Task: Имеется группа студентов (характеристики: Имя, Фамилия, Пол,
# опыт в программировании, 5 оценок по 10-бальной системе и оценка за
# экзамен по 10-бальной системе.
#   Необходимые команды:
# 1) Средняя оценка за домашние задания и экзамен по всей группе;
# 2) Средняя оценка по параметрам, которые были выбраны пользователем
#
##################################################################
#   Использованные процедуры:
# 1) average_by_group
# 2) average_custom
# 3)
# 4)

###################################################################
# Исходные данные
###################################################################
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
# Функция average_by_group
###################################################################
def average_by_group(students, option):
    def count_avg_by_person(student):
            avg_homework = 0
            avg_exam = student["Exam"]
            homework_marks = student["Homeworks"]
            count_marks = 0
            for mark in homework_marks:
                count_marks += 1
                avg_homework += mark
            avg_homework /=count_marks
            return avg_homework, avg_exam 


    def coutn_by_group(students):
        pass
    
    if option == "G":
        avg_homework_males = 0
        avg_exam_males = 0
        count_males = 0
        avg_homework_females = 0
        avg_exam_females = 0
        count_females = 0
        for student in students:
            avg_homework_by_person, avg_exam_by_person = count_avg_by_person(student)
            if student["Gender"] == "M":
                avg_homework_males += avg_homework_by_person
                avg_exam_males += avg_exam_by_person
                count_males += 1
            elif student["Gender"] == "F":
                avg_homework_females += avg_homework_by_person
                avg_exam_females += avg_exam_by_person
                count_females += 1    
        avg_homework_males /= count_males
        avg_exam_males /= count_males
        avg_homework_females /= count_females
        avg_exam_females /= count_females
        return avg_homework_males, avg_exam_males, avg_homework_females, avg_exam_females
    
    elif option == "E":
        avg_homework_experienced = 0
        avg_exam_experienced = 0
        count_experienced = 0
        avg_homework_unexperienced = 0
        avg_exam_unexperienced = 0
        count_unexperienced = 0
        for student in students:
            avg_homework_by_person, avg_exam_by_person = count_avg_by_person(student)
            if student["Experienced"] == True:
                avg_homework_experienced += avg_homework_by_person
                avg_exam_experienced += avg_exam_by_person
                count_experienced += 1
            elif student["Unexperienced"] == False:
                avg_homework_unexperienced += avg_homework_by_person
                avg_exam_unexperienced += avg_exam_by_person
                count_unexperienced += 1    
        avg_homework_males /= count_males
        avg_exam_males /= count_males
        avg_homework_females /= count_females
        avg_exam_females /= count_females
        return avg_homework_males, avg_exam_males, avg_homework_females, avg_exam_females
    else:
        avg_homework_by_group = 0
        avg_exam_by_group = 0
        count_students = 0
        for student in students:
            avg_homework_by_person, avg_exam_by_person = count_avg_by_person(student)
            avg_homework_by_group += avg_homework_by_person
            avg_exam_by_group += avg_exam_by_person
            count_students+=1    
        avg_homework_by_group/=count_students
        avg_exam_by_group /= count_students
        return avg_homework_by_group, avg_exam_by_group


###################################################################
# Функция customise_average
###################################################################
def customise_average():
    option = input("Введите параметр выборки([G]ender / [E]xperienced):").upper()
    if option == "G" | option == "E":
        average_by_group(students, option)
    else:
        print("Введен неверный параметр. Повторите ввод.")
        customise_average()



###################################################################
# Функция main
###################################################################
def main():
    print("Средняя оценка за домашние задания: {}\nСредняя оценка за экзамен: {}".format(*average_by_group(students,"default")))
    print("Средняя оценка за домашние задания у мужчин: {}\nСредняя оценка за экзамен у мужчин: {}\n\n\
Средняя оценка за домашние задания у женщин: {}\nСредняя оценка за экзамен у женщин: {}".format(*average_by_group(students,"G")))

main()









































