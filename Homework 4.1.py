# -*- coding: cp1251 -*-
#######################################################################
# Homework 4.1 ��������� ������ ��� ���������
#######################################################################
# ����������� �������:
#   p - people - ���������� ����� ��������� � ������� ��� ��������
#   l - list - ������� ��� ��������� � �������: ���, �����, ��� ���������
#   s - shelf - ���������� ����� ��������� � ������� ����� �����
#   a - add - ���������� ������ ���������
#   d - delete - �������� ���������
#   m - move - ����������� ���������
#   as - add shelf - ���������� �����
#######################################################################
# �������������� ������������:
#   1)find_owner - ��������� ����� ��������� � ������� ��� ���������
#   2)show_all - ������� ��� ��������� ���������
#   3)find_shelf - ��������� ����� ��������� � ������� ����� �����,
# ��� �� ���������  
#   4)add_new_document - ��������� ��� ���������, ����� ���������,
# ��� ��������� � ����� �����. ������� ������ � ��������� � ���������
# ��� �� �����
#   5)delete_document - ��������� ����� ��������� � ������� ��� �� ��������
# � �����
#   6)move_document - ��������� ����� ��������� � ����� �����. ���������
# �������� �� �������� �����
#   7)add_new_shelf - �������� ����� ��� �������� ����������
#   8)user_input - ��������� ������� � ��������� �� ������������
#   9)help_user - ������� ������ ��������� ������
#########################################################################

import sys


#########################################################################
# �������� ������
#########################################################################
documents = [
        {"type": "passport", "number": "2207 876234", "name": "������� ������"},
        {"type": "invoice", "number": "11-2", "name": "�������� ���������"},
        {"type": "insurance", "number": "10006", "name": "�������� ������"}
        ]
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
        }


#######################################################################
# ������� find_owner
#######################################################################
def find_owner(number):
    #����� �� ���� ����������
    for document in documents:
        #���� ������ ����� - ������� ���
        if document["number"] == number:
            return document["name"]


#######################################################################
# ������� show_all
#######################################################################
def show_all():
    #����� ���������� � �����, �� ������� ��� ���������
    for index, document in enumerate(documents):
        shelf_number = find_shelf(document["number"])
        print("{0}. {1} | {2} | {3} | ����� �����: {4}".format(index+1, document["type"], document["number"], document["name"], shelf_number))


#######################################################################
# ������� find_shelf
#######################################################################
def find_shelf(number):
    #����� �� ������
    for shelf in directories.keys():
        #����� �� ���������� �� �����
        for document in directories[shelf]:
            #���� �������� ������ - ������� ����� �����
            if document == number:
                return shelf

            
#######################################################################
#������� ��� ���������� ��������� �� ������������ �����
#######################################################################
def put_on_shelf(document_number):
    shelf = input("������� ����� �����:")
    #�������� ������������� �����
    shelf_exists = directories.get(shelf)
    #���� ���������� - �������� �� �����
    if shelf_exists != None:
        directories[shelf].append(document_number)
    #����� - ���� �� ��� ���, ���� �� ����� ������� ������������ �����
    else:
        print("����� ����� ���")
        put_on_shelf(document_number)


#######################################################################
# ������� add_new_document
#######################################################################
def add_new_document():
    owners_name = input("������� ��� ���������:")
    document_type = input("������� ��� ���������:")
    document_number = input("������� ����� ���������:")
    #���������� ��������� � ������� ����������
    documents.append({"type":document_type, "number":document_number, "name":owners_name})
    #���������� ��������� �� �����
    put_on_shelf(document_number)
    print()
    #����� ������������ �������� ����������
    show_all()


#######################################################################
# ������� move_document
#######################################################################
def move_document(document_number):
    #���������� �����, �� ������� ��������� ��������
    origin_shelf = find_shelf(document_number)
    #���� ����� ��� - �� �������� �� ������
    if origin_shelf == None:
        print("�������� �� ������")
    #����� - ����� ����� ��� ����������� � ���� ����������� ���������
    else:
        put_on_shelf(document_number)
        directories[origin_shelf].remove(document_number)
        print()
        #����� ������������ ��������
        show_all()


#######################################################################
# ������� add_new_shelf
#######################################################################
def add_new_shelf():
    last_shelf = "0"
    for shelf in directories.keys():
        if last_shelf < shelf:
            last_shelf = shelf
    last_shelf = int(last_shelf)+1
    directories[str(last_shelf)] = []
    print()
    for shelf in directories:
        print("����� {0}: {1}".format(shelf, directories[shelf]))


#######################################################################
# ������� delete_document
#######################################################################
def delete_document(document_number):
    shelf = find_shelf(document_number)
    #���� ����� ��� - �� �������� �� ������
    if shelf == None:
        print("�������� �� ������")
    #����� - �������� ���������
    else:
        for document in documents:
            if document["number"] == document_number:
                 documents.remove(document)
        directories[shelf].remove(document_number)
        print()
        #����� ������������ ��������
        show_all()


#######################################################################
# ������� help_user
#######################################################################
def help_user():
    print("�������: \n\
p - people - ���������� ����� ��������� � ������� ��� ��������\n\
l - list - ������� ��� ��������� � �������: ���, �����, ��� ���������\n\
s - shelf - ���������� ����� ��������� � ������� ����� �����\n\
a - add - ���������� ������ ���������\n\
d - delete - �������� ���������\n\
m - move - ����������� ���������\n\
as - add shelf - ���������� �����\n\
h - help - ������� ��� ��������� �������\n\
e - exit - ����� �� ���������")


#######################################################################
# ������� user_input
#######################################################################
def user_input():
    #���������� ������
    command = input("������� �������:")
    if command.lower() == "p":
        #������� people
        document_number = input("������� ����� ���������:")
        owners_name = find_owner(document_number)
        if owners_name == None:
            print("�������� �� ������")
        else:
            print("��� ���������: " +owners_name)
    elif command.lower() == "l":
        #������� list
        show_all()
    elif command.lower() == "s":
        #������� shelf        
        document_number = input("������� ����� ���������:")
        shelf_number = find_shelf(document_number)
        if shelf_number == None:
            print("�������� �� ������")
        else:
            print("����� �����: " +shelf_number)
    elif command.lower() == "m":
        #������� move
        document_number = input("������� ����� ���������:")
        move_document(document_number)
    elif command.lower() == "a":
        #������� add
        add_new_document()
    elif command.lower() == "d":
        #������� delete
        document_number = input("������� ����� ���������:")
        delete_document(document_number)
    elif command.lower() == "as":
        #������� add shelf
        add_new_shelf()
    elif command.lower() == "h":
        #������� ��� ������ ������������
        help_user()
    elif command.lower() == "e":
        #������� ��� ���������� ������
        print("���������� ������. ������� ����� �������")
        input()
        sys.exit()
    else:
        print("�������� �������. �������������� �������� \"h\" ��� ������ ������ ��������� ������")

        
#######################################################################
# ������� main
#######################################################################
def main():
    help_user()
    print("-------------------------------------")
    while True:
        user_input()
        print("-------------------------------------")

main()
