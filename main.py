import random

# Символы используемые для пароля.
ARRAY_SYMBOLS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'q', 'w', 'e', 'r', 't', 'y','u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'o', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V',
    '!', '?'
]

# Получаем кол-во символов

COUNT_SYMBOLS = 4

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

# Запись готового пароля в txt файл

with open('password.txt', 'a') as password_string:
    password_string.write('{} \n'.format(f'{password}'))