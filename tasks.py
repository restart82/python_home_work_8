# 1 - добавление контакта
# 2 - вывод всех
# 3 - поиск по имени
# 4 - изменить данные
# 5 - удалить данные
# 6 - выход

import os

MY_BOOK = 'phone_book.txt'
BUFFER = 'buffer_file.txt'

# Основные задачи
def add_contact(fio, phone_number, phone_book=MY_BOOK):
    with open(phone_book, 'a') as book:
        book.writelines(fio + '\t' + phone_number + '\n')
    book.close()

def show_all_contacts(phone_book=MY_BOOK):
    with open(phone_book, 'r') as book:
        for line in book:
            print(line[:-1])
    book.close()

def search_contact(name, phone_book=MY_BOOK):
    list_name = list(name.split())
    count = 0
    with open(phone_book, 'r') as book:
        for line in book:
            if list_name[0] == line.split()[0] and list_name[1] == line.split()[1]:
                print('Мобильный номер ' + name + ':')
                print(line.split()[2])
                count += 1
        if count == 0:
            print('Номеров по данному запросу НЕТ')
    book.close()

def change_contact(name, phone_book=MY_BOOK):
    list_name = list(name.split())
    count = 0
    with open(phone_book, 'r') as old_book, open(BUFFER, 'w') as new_book:
        for line in old_book:
            if list_name[0] == line.split()[0] and list_name[1] == line.split()[1]:
                new_number = phone_number_input()
                line = (name + '\t' + new_number + '\n')
                count += 1
            new_book.writelines(line)
        if count == 0:
            print('Номеров по данному запросу НЕТ')
    old_book.close()
    new_book.close()
    os.remove(MY_BOOK)
    os.rename(BUFFER, MY_BOOK)

def delete_contact(name, phone_book=MY_BOOK):
    list_name = list(name.split())
    count = 0
    with open(phone_book, 'r') as old_book, open(BUFFER, 'w') as new_book:
        for line in old_book:
            if list_name[0] == line.split()[0] and list_name[1] == line.split()[1]:
                line = ''
                count += 1
            new_book.writelines(line)
        if count == 0:
            print('Номеров по данному запросу НЕТ')
    old_book.close()
    new_book.close()
    os.remove(MY_BOOK)
    os.rename(BUFFER, MY_BOOK)


# Вспомогательные функции
number_lenth = 5

def name_input():
    first_name = input('Введите имя:\t\t')
    last_name = input('Введите фамилию:\t')
    return first_name + ' ' + last_name

def phone_number_input():
    number = input("Введите номер телефона:\t")
    if phone_validate(number):
        return number
    else:
        print("Некорректный номер, попробуйте еще раз...\n(номер должен состоять из цифр и быть " \
              + str(number_lenth) + "-тизначным)")
        return phone_number_input()

def phone_validate(phone_number):
    return len(phone_number) == number_lenth and phone_number.isdigit()
