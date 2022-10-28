# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from unicodedata import digit

def pack(sequence):
    result = ''
    count = 1
    for i in range(len(sequence) - 1):
        if i != len(sequence) - 2:
            if sequence[i] == sequence[i+1]:
                count += 1
            else:
                result += f'{sequence[i]}{count}'
                count = 1
        else:
            if sequence[i] == sequence[i+1]:
                result += f'{sequence[i]}{count + 1}'
            else:
                result += f'{sequence[i]}{count}' + f'{sequence[i+1]}1'
    return result


def unpack(cipher):
    count = ''
    letter = ''
    result = ''
    i = 0
    while i < len(cipher) - 1:
        if not cipher[i].isdigit():
            letter = cipher[i]
            i += 1
        while i != len(cipher) and cipher[i].isdigit():
            count += cipher[i]
            i += 1     
        result += f'{letter * int(count)}'
        count = ''
    return result


with open('file41.txt', 'r') as data:
    letters = data.readline()

packed_letters = pack(letters)

with open('file42.txt', 'w') as result:
    result.write(packed_letters)

print(unpack(packed_letters))