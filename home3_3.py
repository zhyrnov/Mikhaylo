# Напишите программу, запрашивающую имя, фамилия, отчество и номер группы
# студента и выводящую введённые данные в следующем виде
# ************************************
# *Лабораторная работа № 1   *
# *Выполнил(а): ст. гр. ЗИ-123 *
# *Иванов Андрей Петрович    *
# ************************************
# Необходимо, чтобы программа сама определяла нужную длину рамки.
# Сама же длина рамки зависит от длины наибольшей строки внутри рамки.
# Используя циклы for легко можно выровнять стороны рамки.


def return_example():
    Title = 'laboratorna rabota #3'

    name = input('full name')

    group = input('group:')

    len_tittle = len(Title)
    len_name = len(name)
    len_group = len(group)

    if len_tittle > len_name and len_tittle > len_group:
        max_len = len_tittle
    elif len_name > len_tittle and len_name > len_group:
        max_len = len_name
    else:
        max_len = len_group

        print('*' * (max_len + 4))
        print('*' * (max_len - len_group))

