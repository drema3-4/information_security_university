rus = 'аеорсухАВЕКОРСТХ'
eng = 'aeopcyxABEKOPCTX'

def crypt(path_text: str, path_container: str, path_hide: str) -> None:
    f_txt = open(path_text, 'rb')
    f_cnt = open(path_container, 'r', encoding='cp1251')

    
    cnt = f_cnt.read()
    cnt = list(cnt)
    f_cnt.close()

    index = 0
    b = f_txt.read(1)
    while b:
        code = '{:0>8b}'.format(sum(b))

        for bit in code:
            if bit == '1':

                while cnt[index] not in rus:
                    index += 1
                cnt[index] = eng[rus.find(cnt[index])]
                index += 1

            else:
                while cnt[index] not in rus:
                    index += 1
                index += 1
        
        b = f_txt.read(1)

    f_txt.close()

    f_hide = open(path_hide, 'w', encoding='cp1251')
    f_hide.write(''.join(cnt))
    f_hide.close()

crypt('./text.txt', './container.txt', './hide.txt')