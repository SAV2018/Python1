'''
Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются элементы с индексами 0 и 1,
2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

i = 0
list1 = []
list2 = []
elem = ' '

print('Input some elements of list. Press Enter to exit...')

while True:
    elem = input(' > ')
    if elem == '':  # если нажата клавиша Enter - выход из цикла
        break

    list1.append(elem)
    list2.append(elem)
    if i % 2 == 1:  # если индекс нечётный - меняем значения соедних элементов местами
        list2[i-1], list2[i] = list1[i], list1[i-1]

    i += 1

    #print(list1)
    #print(list2)

print('\nResults:')
print(list1)
print(list2)