import random
import datetime
import os

version = "0.0.1"
# Символы используемые для пароля.
ARRAY_SYMBOLS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'q', 'w', 'e', 'r', 't', 'y','u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'o', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'm',
    '!', '?'
]

# Получаем кол-во символов

COUNT_SYMBOLS = 4
print(f'Версия: {version}')
input_count = input("Введите кол во символов в пароле: ")
if input_count.isdigit():
    count_symbols = int(input_count)
else:
    print(f'Это не число.')
    count_symbols = COUNT_SYMBOLS

def rand_symbols():
    return ARRAY_SYMBOLS[
        random.randint(0, len(ARRAY_SYMBOLS) - 1)
    ]


print(f'Кол-во доступных символов: {len(ARRAY_SYMBOLS)}')
# print(f'Доступные символы: {ARRAY_SYMBOLS}')

password = ''

# Генерация пароля

for i in range(0, count_symbols):
    password = password + f'{rand_symbols()}'

print(f'Пароль: {password}')

text_datetime = f'{datetime.datetime.now()}'

symbols_replace = ['-', ':', ' ', '.']
filename = ''
for s in text_datetime:
    is_write = True
    for sr in symbols_replace:
        if s == sr:
            filename += '_'
            is_write = False

    if is_write:
        filename += s
# Запись готового пароля в txt файл
if not os.path.exists('passwords'):
    os.mkdir('passwords')

with open(f'passwords/{filename}_pswrd.txt', 'a') as password_string:
    password_string.write('{} \n'.format(f'{password}'))

print(f'Нажмите клавишу ENTER чтобы закрыть')
input()
