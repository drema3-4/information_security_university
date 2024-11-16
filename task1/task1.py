import os
import re

hashs = dict()

def hash_for_file(path: str) -> int:
    f = open(path, 'rb')
    
    hash = int('0b{:0>8b}'.format(sum(f.read(1))) + '{:0>8b}'.format(sum(f.read(1))), 2)

    t1 = f.read(1)
    t2 = f.read(1)
    while t1 or t2:
        hash ^= int('0b{:0>8b}'.format(sum(t1)) + '{:0>8b}'.format(sum(t2)), 2)

        t1 = f.read(1)
        t2 = f.read(1)
    
    return hash

def hash_for_files(path: str, hashs: dict) -> dict:
    files_and_dirs = os.listdir(path)

    if files_and_dirs:

        pattern = re.compile(r'\w*\.[a-zA-z]*')

        for i in files_and_dirs:
            if i == 'hash.txt' or i == 'task1.py':
                continue
            else:
                if pattern.match(i):
                    hashs[path + i] = hash_for_file(path + i)
                else:
                    hash_for_files(path + i + '/', hashs)
    
    else:

        hashs[path] = 0

    return hashs

def calc_control(path: str):
    hash = hash_for_files(path, dict())

    f = open(path + 'hash.txt', 'w')
    
    for i in hash:
        f.write(i + ':' + str(hash[i]) + '\n')
    
    f.close()

def check(path: str):
    if os.path.exists(path + 'hash.txt'):
        hash = dict()

        f = open(path + 'hash.txt', 'r')
        
        for i in f.read().splitlines():
            temp = i.split(':')
            hash[temp[0]] = eval(temp[1])

        f.close()

        new = hash_for_files(path, dict())

        flag = True

        for i in new:
            if i in hash:
                if hash[i] != new[i]:
                    print(i + ': old = {0} : new = {1}'.format(hash[i], new[i]))
                    flag = False
            else:
                print(i + ': {0}'.format(new[i]))
                flag = False

        for i in hash:
            if i not in new:
                print(i + ': delete')

        if flag:
            print('Никаких изменений не было!')

    else:
        print('Нет контрольных данных, проверка невозможна!')

temp = ''

while temp != 'stop':
    if temp == 'calc':
        calc_control('./')
        print('done!')
    elif temp == 'check':
        check('./')
        print('done!')
    temp = input('>> ')