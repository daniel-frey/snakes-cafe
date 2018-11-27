from textwrap import dedent
import sys

WIDTH = 60
MENU = {
    'Appetizers': ['Wings', 'Cookies','Spring Rolls'],
    'Entrees': ['Salmon', 'Steak', 'Meat Tornado?', 'A Literal Garden'],
    'Desserts': ['Ice Cream', 'Pie', 'Cake'],
    'Drinks': ['Coffee', 'Tea', 'Blood of the Innocent'],
    }


def welcome():
    """This function will display the opening message as well as the menu to the user."""

    ln_one = 'Welcome to the Snakes Cafe!'
    ln_two = 'Please see our menu below.'
    ln_three = 'To quit at any time, type "quit"'

    print(dedent(f'''
    {'*' * WIDTH}
    {(' '* ((WIDTH - len(ln_one)) // 2)) + ln_one + (' ' * ((WIDTH - len(ln_one)) // 2))}
    {(' '* ((WIDTH - len(ln_two)) // 2)) + ln_two + (' ' * ((WIDTH - len(ln_two)) // 2))}
    {(' '* ((WIDTH - len(ln_three)) // 2)) + ln_three + (' ' * ((WIDTH - len(ln_three)) // 2))}
    {'*' * WIDTH}
    '''))

    # for the keys and values in the MENU we will print both and then prompt the user for their order
    for k, v in MENU.items():
        print(k)
        print('--' * 5)
        for item in v:
            print(item)
            print()

    print('*' * 35)
    print('** What would you like to order? **')
    print('*' * 35)


def check_input(user_input, menu):
    if user_input.lower() == 'quit':
        exit()
        return
    for k, v in menu.items():
        for item in v:
            if user_input.lower() == item.lower():
                return True
    else:
        return False

def question_prompt():
    return input()

def exit():
    print(dedent('''
    Thank you for your order!'''))
    sys.exit()

def run():
    welcome()
    order_items = 0

    while True:
        order_list = []
        menu_order = question_prompt()
        if check_input(menu_order, MENU) is True:
            order_list.append(menu_order)
            if menu_order in order_list:
                order_items += 1
                print('{} has been added to your current order'.format(menu_order))
                print('Your order contains {} items'.format(order_items))
                print(' \n')
        else:
            question_prompt()


if __name__ == '__main__':
    run()
