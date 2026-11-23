import random
while True:
    print('Добро пожаловать в числовую угадайку!')
    def is_value(u):
        if 1 <= int(u) <= right:
            u = int(u)
            return u
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            u = int(u)
            return u
    print('Выберите правую границу для случайного выбора числа')
    right = int(input())
    n = random.randint(1, right)
    print("Введите число от 1 до 100")
    p = 0
    while True:
        u = input()
        u = is_value(u)
        if 1 > u or u > 100:
            continue
        if u == n:
            p += 1
            print("Вы угадали, поздравляем!")
            break
        if u < n:
            p += 1
            print("Ваше число меньше загаданного, попробуйте еще разок")
            continue
        if u > n:
            p += 1
            print("Ваше число больше загаданного, попробуйте еще разок")
            continue
    print("Количество попыток:",p)
    print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
