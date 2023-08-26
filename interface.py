from main import *

instruction = 'Выберите действие: \n' \
            '\t1 - Записать данные в файл \n\t2 - Печать всех данных \n' \
            '\t3 - Поиск по имени и фамилии \n\t4 - Изменить строку \n' \
            '\t5 - Удалить строку\n\t6 - Остановить программу \n'
comand = 1

def clear_if(comand):
    if comand not in ('2', '3'):
        return clear()

while True:
    clear_if(comand)
    print(instruction)
    comand = input("Введите команду --> ")
    clear_if(comand)
    init_tasks(comand)
