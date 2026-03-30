import os
import sys


# Функція для визначення шляху до файлів (для EXE)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def sortirovka():
    stan = True
    while stan:
        jopka = []
        vvid_koristovacha = input("Введіть кількість чисел (або /stop для виходу): ")

        if vvid_koristovacha == "/stop":
            print("Сортування завершено")
            break

        try:
            a = int(vvid_koristovacha)
            counter = 0
            while a > counter:
                counter = counter + 1
                vvid = int(input(f"Введіть число {counter}: "))
                jopka.append(vvid)

            # Bubble Sort
            for i in range(len(jopka)):
                for j in range(len(jopka)):
                    if jopka[i] < jopka[j]:
                        jopka[i], jopka[j] = jopka[j], jopka[i]

            print(f"Результат сортування: {jopka}")
        except ValueError:
            print("Будь ласка, вводьте тільки числа!")


def rahuvalnyk():
    stan = True
    while stan:
        a = input("Enter any word (or /stop): ")

        if a == "/stop":
            print("Program ended")
            break

        res = len(a)
        print("Length of ur word: ", res)

        for i in a:
            print(i)


def calc():
    print("Введіть операцію (+ - * /) або /stop: ")
    x1 = input()
    if x1 == "/stop":
        return

    try:
        x2 = float(input("Введіть перше число: "))
        x3 = float(input("Введіть друге число: "))

        if x1 == "+":
            print(f"Результат: {x2 + x3}")
        elif x1 == "-":
            print(f"Результат: {x2 - x3}")
        elif x1 == "*":
            print(f"Результат: {x2 * x3}")
        elif x1 == "/":
            if x3 != 0:
                print(f"Результат: {x2 / x3}")
            else:
                print("На нуль ділити не можна!")
    except ValueError:
        print("Помилка: треба вводити числа!")


def open_media():
    # ВИПРАВЛЕНО: назви точно як на твоїх скріншотах
    image_path = resource_path("konor.jpg")
    music_path = resource_path("popalsya.MP3")

    print("Перевірка файлів...")
    if os.path.exists(image_path):
        os.startfile(image_path)
    else:
        print(f"Файл {image_path} не знайдено!")

    if os.path.exists(music_path):
        os.startfile(music_path)
    else:
        print(f"Файл {music_path} не знайдено!")


# --- ГОЛОВНИЙ ЦИКЛ EASYOS ---
print("Вітаємо в EasyOS")
stanprocess = True

while stanprocess:
    print("\n--- МЕНЮ ---")
    print("1. Справочник")
    print("2. Калькулятор")
    print("3. Рахувальник")
    print("4. Сортировка")
    print("------------")

    # ВИПРАВЛЕНО: input без int(), щоб пасхалка працювала
    maininput = input("Оберіть програму: ")

    if maininput == "2":
        print("===============")
        calc()
        print("===============")
    elif maininput == "1":
        print("---------------")
        print("EasyOS Справочник")
        print("Командування виконується через термінал.")
        print("Щоб вийти з підпрограми, пишіть /stop")
        print("Пасхалка: введіть секретну фразу в головному меню.")
        print("---------------")
    elif maininput == "3":
        print("===============")
        rahuvalnyk()
        print("===============")
    elif maininput == "4":
        print("===============")
        sortirovka()
        print("===============")
    elif maininput == "єбу діток":  # ТВОЯ ПАСХАЛКА
        open_media()
    elif maininput == "/exit":
        print("Вихід з EasyOS...")
        break
    else:
        print("Невідома команда!")