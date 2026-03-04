def task1():
    s = "Welcome to Python!"
    result = s.replace(" ", "_")
    print(result)


def task2():
    s = input("Введите строку: ")
    words = s.split()
    print("Количество слов:", len(words))


def task3():
    s = input("Введите предложение: ")
    words = s.split()

    result = []
    for word in words:
        result.append(word[::-1])

    print(" ".join(result))


def task4():
    s1 = input("Первая строка: ")
    s2 = input("Вторая строка: ")

    result = False

    for i in range(len(s1)):
        new_string = s1[:i] + s1[i+1:]
        if new_string == s2:
            result = True
            break

    print(result)


def task5():
    s1 = input("Первая строка: ")
    s2 = input("Вторая строка: ")

    longest = ""

    for i in range(len(s1)):
        for j in range(i + 1, len(s1) + 1):
            substring = s1[i:j]

            if substring in s2 and len(substring) > len(longest):
                longest = substring

    print("Самая длинная общая подстрока:", longest)


print("Выберите задание:")
print("1 - Замена пробелов")
print("2 - Подсчёт слов")
print("3 - Перевернуть слова")
print("4 - Удаление одного символа")
print("5 - Самая длинная общая подстрока")

choice = int(input("Введите номер задания: "))


match choice:
    case 1:
        task1()
    case 2:
        task2()
    case 3:
        task3()
    case 4:
        task4()
    case 5:
        task5()
    case _:
        print("Неверный номер задания")
