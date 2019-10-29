'''
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

action = ''
while action == '':
    # словарь соответствия месяцев временам года
    months_dic = {1:'зима', 2:'зима', 3:'весна', 4:'весна', 5:'весна', 6:'лето',
                  7:'лето', 8:'лето', 9:'осень', 10:'осень', 11:'осень', 12:'зима'}
    # список соответствия месяцев временам года
    months_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']

    month = int(input('\nEnter number of month: '))

    if 1 <= month <= 12:
        print(f'From dict:\tMonth #{month} - {months_dic[month]}')
        print(f'From list:\tMonth #{month} - {months_list[month-1]}')
    else:
        print('\nIncorrect number of month (should be from 1 to 12)')

    action = input('\nPress Enter to continue, any key to exit... ')