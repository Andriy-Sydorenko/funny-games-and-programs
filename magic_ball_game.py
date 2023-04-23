import random
from pyfiglet import Figlet

preview_text = Figlet(font="slant", justify="right")
print(preview_text.renderText("Magic Ball"))
username = input("Як тебе звати?: ")
print("Привіт,", username)


def menu():
    mn = int(input("Що ти хочеш зробити?\n1 - зіграти в кулю\n2 - вийти з кулі\n"))
    if mn == 1:
        game()
    elif mn == 2:
        quit()
    else:
        print("Не те число!!")
        menu()


def game():
    answers = ["Безсумнівно", "Здається, ТАК!", "Поки неясно, спробуй ще раз", "Навіть не думай!!",
               "Вже вирішено!", "Скоріш за все", "Запитай пізніше", "Моя відповідь - НІ",
               "Безсумнівно", "Гарні перспективи", "Краще не розповідати", "За моїми даними - НІ",
               "Однозначно ТАК", "Знаки кажуть - ТАК", "Зараз не можна сказати точно", "Перспективи не дуже гарні",
               "Можеш бути впевненим у цьому", "ТАК", "Сконцентруйся та запитай знову", "Точно НІ"]
    question = input("Задай своє запитання, смертний: ")
    print(random.choice(answers), end="\n\n")
    gn = input("Задоволений відповіддю?\nт - так\nн - н\n")
    if gn.lower() == "т" or gn.lower() == "так":
        print("Чудово!\n")
        menu()
    elif  gn.lower() == "н" or gn.lower() == "ні":
        print("Ну, кожному своє\n")
        menu()

menu()