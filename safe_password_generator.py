import random

digits = list("0123456789")
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
punctuation = list("!#$%&*+-=?@^_")
char_list = []
psswrd = ""
p_l = []

ps_num = int(input("Введіть кількість паролів які ви хочете згенерувати: "))
ps_len = int(input("Введіть довжину пароля: "))
ps_dg = int(input("Включати цифри в паролях?\n1 - так\n2 - ні\n"))
ps_alp = int(input("Включати літери в паролях?\n1 - так\n2 - ні\n"))
ps_sym = int(input("Включати символи в паролях?\n1 - так\n2 - ні\n"))

if ps_dg == 1:
    char_list += digits
if ps_alp == 1:
    char_list += letters
if ps_sym == 1:
    char_list += punctuation

for i in range(ps_num):
    while len(psswrd) != ps_len:
        psswrd += psswrd.join(random.choice(char_list))
    p_l.append(psswrd)
    psswrd = ""

for i in p_l:
    print(i)