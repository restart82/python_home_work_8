from main import *

instruction = 'Выберите действие: \n\t1 - Записать данные в файл \n\t2 - Печать всех данных \n\t3 - Поиск по имени и фамилии \n\t4 - Остановить программу'
comand = 1

while True:
    if comand not in ('2', '3'):
        clear()
    print(instruction)
    comand = input("Введите команду --> ")
    if comand not in ('2', '3'):
        clear()
    init_tasks(comand)
