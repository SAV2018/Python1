import tkinter
import PIL
import os
import psutil
import sys
import shutil

# print('Test v.1')
# print('hello')
# print(10/3)
# print(10//3)
# print(10%3)
# print(10**3)
# print(10*3+1)
# print(10*(3+1))
#name = input('Input your name: ')
#print('Hello, ', name)

def duplicate_file(f):
    result = False
    if os.path.isfile(f):
        file = (f + '.dupl')
        shutil.copy(f, file)
        result = os.path.isfile(file)
        if result:
            print('File ', file, ' has been duplicated')
        else:
            print('File not duplicated')
    return result

def main():
    # PEP-8
    answer = 'Y'
    while (answer != 'Q'):
        print('Choose action: ')
        print(' [1] print list of files')
        print(' [2] print info about system')
        print(' [3] print pids')
        print(' [4] douplicate files of curdir')
        action = int(input('Your choice [1-4]: '))
        if action == 1:
            print(os.listdir())
        elif action == 2:
            print('System info: ', os.name, os.curdir, os.getcwd(), sys.platform, sys.version, sys.winver,
                  os.cpu_count(), sys.getfilesystemencoding(), os.getlogin())
        elif action == 3:
            print(psutil.pids())
        elif action == 4:
            list = os.listdir()
            for f in list:
                duplicate_file(f)
        else:
            pass
        answer = input('Press [Q] for exit...')

    print('Goodbye!')

if __name__ == '__main__':
    main()