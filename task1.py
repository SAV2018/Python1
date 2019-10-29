'''
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''

mlist = [23, 'This is some text.', 5.532, True, [1, 2, 'd', 3], None, ('On', 'Off'), {"id":1, "n":10}, {1, 2, 3, 4}]

for element in mlist:
    print(f'{str(element).ljust(18)}\t:\t{type(element)}')