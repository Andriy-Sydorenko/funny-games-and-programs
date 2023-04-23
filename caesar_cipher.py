from pyfiglet import Figlet

preview_text = Figlet(font="slant", justify="right")
print(preview_text.renderText("Caesar Cipher"))

ukr_al = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюяабвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
en_al = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"


def encrypt():
    lang = int(input("Яку мову хочете обрати?\n1 - українську\n2 - англійську\n"))
    shift = int(input("Який здвиг буде у шифрі?: "))
    txt = input("Введіть текст який хочете зашифрувати:\n")
    enc_txt = ""
    if lang == 1:
        for i in txt:
            i = ukr_al[ukr_al.find(i) + shift]
            enc_txt += i
    elif lang == 2:
        for i in txt:
            i = en_al[en_al.find(i) + shift]
            enc_txt += i
    else:
        print("Виберіть існуючу опцію!")
        encrypt()
    print("Ваш заширований текст: ", enc_txt)


def decrypt():
    lang = int(input("Яку мову хочете обрати?\n1 - українську\n2 - англійську\n"))
    shift = int(input("Який здвиг буде у шифрі?: "))
    txt = input("Введіть текст який хочете розшифрувати:\n")
    dec_txt = ""
    if lang == 1:
        for i in txt:
            i = ukr_al[ukr_al.find(i) - shift]
            dec_txt += i
    elif lang == 2:
        for i in txt:
            i = en_al[en_al.find(i) - shift]
            dec_txt += i
    else:
        print("Виберіть існуючу опцію!")
        encrypt()
    print("Ваш розширований текст: ", dec_txt)


def menu():
    opt = int(input("Що ви хочете зробити?\n1 - зашифрувати слово\n2 - розшифрувати слово\n3 - закрити програму\n"))
    if opt == 1:
        encrypt()
    elif opt == 2:
        decrypt()
    elif opt == 3:
        quit()
    else:
        print("Введіть правильне число!")
        menu()

menu()
