'''
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
'''

str = input('\nEnter a string of several words (with spaces): ')

for i, word in enumerate(str.split(), 1):
    etc = ('', '…')[len(word)>10]   # если больше 10 символов в слове - ставим маркер обреза
    print(f' {i}.\t{word[:10]}{etc}')