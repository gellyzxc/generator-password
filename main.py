import random
import datetime
import os
from rich.box import ROUNDED
from Password import Password
from rich import print
from rich.layout import Layout
from rich.panel import Panel
from rich.console import Group, Console
from rich.text import Text
from rich import box
from rich.style import Style
from rich.table import Table



password = Password()

def random_symbols():
    return password.ARRAY_SYMBOLS[
        random.randint(0, len(password.ARRAY_SYMBOLS) - 1)
    ]

def file_name():

    text_datetime = f'{datetime.datetime.now()}'

    symbols_replace = ['-', ':', ' ', '.']
    fn = ''
    for s in text_datetime:
        is_write = True
        for sr in symbols_replace:
            if s == sr:
                fn += '_'
                is_write = False

        if is_write:
            fn += s
    return fn

count_symbols = input("Введите кол во символов: ")
pin_code = input("Введите пин-код для пароля: ")

if not pin_code.isdigit():
    pin_code = None

if count_symbols.isdigit():
    password.generate(int(count_symbols), pin_code)
else:
    password.generate(None, None)


if not os.path.exists('passwords'):
    os.mkdir('passwords')

with open(f'passwords/{file_name()}_pswrd.txt', 'a') as password_string:
    password_string.write('{} \n'.format(f'{password.check_summa}'))



console = Console()
layout = Layout(name="info")
layout["info"].size = 1
table_info = Table.grid(padding=1)

textstyle = Style(color="red", italic=True)
bgstyle = Style(bgcolor="blue")

print_cas = Text.from_markup(
    f'{len(password.get_array_symbols())}',
    style=textstyle
)
table_info.add_row(f'Кол во доступных символов:', print_cas)

print_cv = Text.from_markup(
    f'{password.count_variants}',
    style=textstyle
)
table_info.add_row(f'Кол во доступных комбинаций:', print_cv)

print_pin = Text.from_markup(
    f'{pin_code}',
    style=textstyle
)
table_info.add_row(f'Пин-код:', print_pin)

print_password = Text.from_markup(
    f'{password.password}',
    style=textstyle
)
table_info.add_row(f'Сгенерированный пароль:', print_password)

print_checksum = Text.from_markup(
    f'Ключ пароля: {password.check_summa}',
    style=textstyle
)


layout.update(
    Panel(
        Group(
            table_info,
            "",
            print_checksum

        ),
        title="generator paroley",
        subtitle="made by gellyzxc | ver 0.0.6",
        box=box.ROUNDED,
        style=bgstyle,
    )
)
os.system('cls||clear')
print(layout)
input()
