'''
Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются элементы с индексами 0 и 1,
2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

list1 = []
list2 = []
element = ' '
i = 0   # индекс элемента

print('Input some elements of list. Press Enter to exit...')

while True:
    element = input(' > ')
    if element == '':  # если нажата клавиша Enter - выход из цикла
        break

    list1.append(element)
    list2.append(element)
    if i % 2 == 1:  # если индекс нечётный - меняем значения соедних элементов местами
        list2[i-1], list2[i] = list1[i], list1[i-1]

    i += 1

    #print(list1)
    #print(list2)

print('\nResults:')
print(list1)
print(list2)