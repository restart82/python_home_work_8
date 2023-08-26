import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

from tasks import *

# ЗАПУСК ПРОГРАММЫ ЧЕРЕЗ INTERFACE.PY

def init_tasks(task):
    match task:
        case '1':
            add_contact(name_input(), phone_number_input())
        case '2':
            print("Текущее состояние телефонной книги:")
            show_all_contacts()
            print('\n')
        case '3':
            search_contact(name_input())
        case '4':
            change_contact(name_input())
        case '5':
            delete_contact(name_input())
        case '6':
            clear()
            exit()
        case _:
            print("Неверная команда")
