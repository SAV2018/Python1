'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
'''

def print_userdata(name, family, town, year, phone, email=''):
    '''
    Печать данных пользователя
    :param name: str
    :param family: str
    :param town: str
    :param year: int
    :param phone: str
    :param email: str
    :return:
    '''
    print(f'{name + " " + family:25}\t({year})\t{town:15}\t{phone:16}\t{email}')

print()
print_userdata(name='Tom', family='Clancy', year=1978, town='London', email='mail@gmail.com', phone='(000) 100-10-10')
print_userdata(name='Jhon', family='Richard', year=1986, town='Torn', phone='(999) 999-99-99')