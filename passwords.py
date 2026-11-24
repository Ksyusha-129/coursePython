import random
def generate_password(length, chars):
    passw = ''
    for i in range(length):
        passw += random.choice(chars)
    return passw

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''
print("Введите требуемое количество паролей для генерации")
quantity = int(input())
print("Введите длину требуемого пароля")
length = int(input())
print("Включать ли цифры 0123456789?")
if input().strip().lower() == "да":
    chars += digits
print("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ?")
if input().strip().lower() == "да":
    chars += uppercase_letters
print("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ?")
if input().strip().lower() == "да":
    chars += lowercase_letters
print("Включать ли символы !#$%&*+-=?@^_ ?")
if input().strip().lower() == "да":
    chars += punctuation
print("Исключать ли неоднозначные символы il1Lo0O ?")
if input().strip().lower() == "да":
    for g in "il1Lo0O":
        chars.replace(g, "")
for i in range(quantity):
    print(generate_password(length, chars))