def crypt(path_text: str, path_container: str, path_hide: str) -> None:
    f_txt = open(path_text, 'rb')
    f_cnt = open(path_container, 'r', encoding='cp1251')
    
    cnt = f_cnt.read()
    cnt.replace('   ', ' ')
    cnt.replace('  ', ' ')
    cnt = list(cnt)
    f_cnt.close()

    index = 0
    b = f_txt.read(1)
    while b:
        code = '{:0>8b}'.format(sum(b))

        for b in code:
            if b == '1':
                while cnt[index] != ' ':
                    index += 1
                
                cnt[index] = '  '
                index += 1
            else:
                while cnt[index] != ' ':
                    index += 1
                index += 1

        b = f_txt.read(1)

    f_hide = open(path_hide, 'w', encoding='cp1251')
    f_hide.write(''.join(cnt))

crypt('./text.txt', './container.txt', './hide.txt')