from sys import argv


def add_sale(sale):
    """
    :param sale:
    :return: nothing, append sale to the file
    """
    with open('bakery.csv', 'a', encoding='utf-8', newline='') as backery:
        backery.writelines(f'{str(sale)}\n')
        return 'Done'


def show_sales(*args):
    """
    Show file
    :return: all file if no args
    """
    with open('bakery.csv', 'r', encoding='utf-8') as file:
        if args == ():
            for line in file:
                print(line, end='')
        elif len(args) == 1:
            file.seek(0)
            for count, line in enumerate(file):
                if count >= int(args[0]) - 1:
                    print(line, end='')
        elif len(args) == 2:
            file.seek(0)
            for count, line in enumerate(file):
                if count >= int(args[0]) - 1 and count < int(args[1]):
                    print(line, end='')


"""
def edit_sales(*args):
    with open('bakery.csv', 'r+', encoding='utf-8') as file:
        for line, value in enumerate(file):
            if value[:-1] == str(args[0]):
                print('test')
"""

if len(argv) == 1:
    print('Укажите аргументы для запуска:\nadd для добавления суммы\nshow для отображения')
elif argv[1] == 'add':
    add_sale(argv[2])
elif argv[1] == 'show':
    if len(argv) == 2:
        show_sales()
    elif len(argv) == 3:
        show_sales(argv[2])
    elif len(argv) == 4:
        show_sales(argv[2], argv[3])


#python lesson_6_homework_3.py show 10 13