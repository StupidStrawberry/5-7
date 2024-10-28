import random


def generate_string(length):
    alphabet = "йцукенгшщзхъэждлорпавыфячсмитьбюqwertyuioplkjhgfdsazxcvbnm"
    string = ""
    for i in range(length):
        x = random.randint(0, 57)
        string += alphabet[x]
    return string


print(generate_string(12))
