alphabet = 'абвгдеёжзийклмнопртсуфхцчшщъыьэюя'

def __make_matrix__(alphabet: str) -> list[str]:
    size = len(alphabet)

    matrix = []
    for i in range(size):
        matrix.append(alphabet[i:] + alphabet[:i])

    return matrix

def __make_sub_matrix__(key: str) -> list[str]:
    matrix = __make_matrix__(alphabet)
    sub_matrix = []
    
    sub_matrix.append(matrix[0])

    for i in key:
        for j in matrix:
            if j[0] == i:
                sub_matrix.append(j)
                break

    return sub_matrix

def encryption(key: str, path_text: str, path_crypt: str) -> None:
    temp = ''
    sub_matrix =__make_sub_matrix__(key)
    text = open(path_text, 'r').read()

    index = 0
    for i in text:
        if i in alphabet:
            temp += key[index]
            ++index
        else:
            temp += i

    new = ''

    for i in range(len(text)):
        if temp[i] in key:
            t1 = sub_matrix[0]
            t2 = ''
            
            for j in sub_matrix:
                if j[0] == temp[i]:
                    t2 = j
                    break

            new += t2[t1.index(text[i])]

        else:
            new += temp[i]

    open(path_crypt, 'w').write(new)

def dectyption(key: str, path_crypt: str, path_decrypt: str) -> str:
    sub_matrix = __make_sub_matrix__(key)
    temp = ''
    text = open(path_crypt, 'r').read()

    index = 0
    for i in text:
        if i in alphabet:
            temp += key[index]
            ++index
        else:
            temp += i

    new = ''

    for i in range(len(text)):
        if temp[i] in key:
            t1 = sub_matrix[0]
            t2 = ''
            
            for j in sub_matrix:
                if j[0] == temp[i]:
                    t2 = j
                    break

            new += t1[t2.index(text[i])]

        else:
            new += temp[i]

    open(path_decrypt, 'w').write(new)

temp = '1'

path_text = './task3/text.txt'
path_crypt = './task3/crypt.txt'
path_decrypt = './task3/decrypt.txt'

while temp != '0':
    key = input('Enter the key\n>> ')
    input('encryption >> ?')
    encryption(key, path_text, path_crypt)
    input('decription >> ?')
    dectyption(key, path_crypt, path_decrypt)
    temp = input('>> ')