import random


def generate_string(length):
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    string = ""
    for i in range(length):
        x = random.randint(0, 115)
        string += alphabet[x]
    print(string)
    return string


def get_string():
    print("Введите строку")
    string = str(input())
    return string


def crypto(string):
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    print("Введите сдвиг")
    move = int(input())
    new_string = ""
    for i in range (len(string)):
        for x in range (len(alphabet)):
            if string[i] == alphabet[x]:
                if x + move <= 115:
                    new_string += alphabet[x + move]
                else:
                    new_string += alphabet[x + move - 115]
    return new_string


def print_crypto(string):
    if string == "":
        print("Сначала измените строку")
        return 0
    else:
        print(string)
        return 1


def end():
    exit(0)


def menu():
    string = ""
    new_string = ""
    while True:
        print("Выберете пункт меню\n1-Ввод строки самостоятельно 2-Генерация строки случайно 3-Шифровка строки 4-Вывод строки 5-Выход")
        a = int(input())
        match a:
            case 1:
                string = str(input())
            case 2:
                print("Введите длинну строки")
                length = int(input())
                string = generate_string(length)
            case 3:
                new_string = crypto(string)
            case 4:
                print_crypto(new_string)
            case 5:
                end()


menu()
