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
#   2)show_all - ������� ��� ��������� ��������� �� ������
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
#########################################################################

import sys

###################################
# �������� ������
###################################
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
    for index, document in enumerate(documents):
        print("{0}. {1} - {2} - {3}".format(index+1, document["type"], \
                                document["number"], document["name"]))


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
h - help user - ������� ��� ��������� �������\n\
e - exit - ����� �� ���������")


#######################################################################
# ������� user_input
#######################################################################
def user_input():
    command = input("������� �������:")
    if command.lower() == "p":
        document_number = input("������� ����� ���������:")
        owners_name = find_owner(document_number)
        print("��� ���������: " +owners_name)
    elif command.lower() == "h":
        help_user()
    elif command.lower() == "e":
        print("���������� ������")
        input()
        sys.exit()
        
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
