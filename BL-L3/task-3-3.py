'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def my_func(arg_1, arg_2, arg_3):
    '''
    Возвращает сумму двух наибольших аргументов
    '''
    return float(arg_2) + float(arg_3)

while True:
    print('\nEnter 3 numbers (separated by spaces). Press Enter to exit...')
    nums = input('> ')
    if nums == '':
        break

    try:
        arg_1, arg_2, arg_3 = sorted(nums.split())
        print(my_func(arg_1, arg_2, arg_3))
    except ValueError:
        print('Incorrect values')
        continue

print('\nProgram completed')