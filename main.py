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
if count_symbols.isdigit():
    password.generate(int(count_symbols))
else:
    password.generate(None)

#---

if not os.path.exists('passwords'):
    os.mkdir('passwords')

with open(f'passwords/{file_name()}_pswrd.txt', 'a') as password_string:
    password_string.write('{} \n'.format(f'{password.password}'))


textstyle = Style(color="magenta", italic=True)
bgstyle = Style(bgcolor="cyan")

print_cas = Text.from_markup(
    f'Кол во доступных символов: {len(password.get_array_symbols())}',
    style=textstyle
)

print_cv = Text.from_markup(
    f'Кол во возможных комбинаций: {password.count_variants}',
    style=textstyle
)

print_password = Text.from_markup(
    f'Сгенерированный пароль: {password.password}',
    style=textstyle
)

console = Console()
layout = Layout(name="info")
layout["info"].size = 1
layout.update(
    Panel(
        Group(
            print_cas, print_cv, print_password
        ),
        title="generator paroley",
        subtitle="made by gellyzxc",
        box=box.ROUNDED,
        style=bgstyle,
    )
)
os.system('cls||clear')
print(layout)
input()