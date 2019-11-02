'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def div_nums(num_1, num_2):
    '''
    Возвращает частное от деления первого числа на второе
    '''
    try:
        result = num_1 / num_2
    except ZeroDivisionError:
        print('Error: second number should not be 0')
        result = None

    return result

while True:
    print('\nEnter 2 numbers: ')
    try:
        num_1 = float(input('> '))
        num_2 = float(input('> '))
    except ValueError:
        print('Incorrect value')
        continue

    print(div_nums(num_1, num_2))
