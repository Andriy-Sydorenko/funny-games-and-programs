import random
from pyfiglet import Figlet

preview_text = Figlet(font="slant", justify="right")
print(preview_text.renderText("Guess The Number Game!"))


def game():
    n = int(input("Вкажіть праву границю для випадкового вибору числа: "))
    num = random.randint(1, n)
    ent_num = int(input("Введіть число: "))
    g_c = 0
    if ent_num in list(range(1, 101)):
        print("Тож, граємо!")
    else:
        print("Таке число не підходить!")
        game()
    while ent_num != num:
        if ent_num < num:
            print("Замало!\n")
            g_c += 1
        elif ent_num > num:
            print("Забагато!\n")
            g_c += 1
        ent_num = int(input("Введіть інше число: "))
    else:
        winner_text = Figlet(font="slant", justify="right")
        print(winner_text.renderText("YOU WIN!"))
        print("Total guesses:", g_c, end="\n\n")
        menu()


def menu():
    mn = int(input("Що ви хочете зробити?\n1 - зіграти в гру\n2 - вийти з гри\n"))
    if mn == 1:
        game()
    elif mn == 2:
        quit()
    else:
        print("Не те число!!")
        menu()


menu()
