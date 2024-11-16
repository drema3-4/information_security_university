def decrypt(path_hide: str, path_decode: str) -> None:
    f_hide = open(path_hide, 'r', encoding='cp1251')
    f_dcd = open(path_decode, 'wb')

    line = f_hide.readline()
    code = '0b'
    while line:
        if line[-2:] == ' \n':
            code += '1'
        else:
            code += '0'

        if len(code) == 10:
            if code == '0b00000000':
                break
            else:
                f_dcd.write(int(code, 2).to_bytes(1))
                code = '0b'

        line = f_hide.readline()

    f_hide.close()
    f_dcd.close()


decrypt('./hide.txt', './decode.txt')