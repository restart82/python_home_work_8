# 1 - добавление контакта
# 2 - вывод всех
# 3 - поиск по имени
# 4 - выход

MY_BOOK = 'phone_book.txt'

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

# Вспомогательные функции
def name_input():
    first_name = input('Введите имя:\t\t')
    last_name = input('Введите фамилию:\t')
    return first_name + ' ' + last_name

def phone_number_input():
    number = input("Введите номер телефона:\t")
    if phone_validate(number):
        return number
    else:
        print("Некорректный номер, попробуйте еще раз...")
        return phone_number_input()

def phone_validate(phone_number):
    return len(phone_number) == 11 and phone_number.isdigit()
