'''
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и
снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
сумме и после этого завершить программу.
'''

def sum_numbers(numbers):
    global stop
    '''
    Проверка и суммирование последовательности чисел
    '''
    sum = 0
    for v in numbers:
        if v == special_char:   # если спецсимвол завершения
            stop = True
            print()
            break
        try:
            sum += float(v)
        except ValueError:
            print(' - Incorrect value')
            sum = 0
            break
    else:
        print(f' => {sum}')

    return sum


special_char = '='  # спецсимвол завершения работы
stop = False        # признак завершения
sum = 0             # сумма

while not stop:
    s = input(f'\nEnter numbers separated by spaces (or \'{special_char}\' to stop):\n> ')
    print(s.split(), end='')

    sum += sum_numbers(s.split())
    print(f'Sum: {sum}')

print('Program completed.')

