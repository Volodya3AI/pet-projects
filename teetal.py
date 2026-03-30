import os
import sys
#головні файли, память
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
        vvid_koristovacha = input("Введіть кількість чисел: ")


        if vvid_koristovacha == "/stop":
            print("Program ended")
            break

        a = int(vvid_koristovacha)
        counter = 0
        while a > counter:
            counter = counter + 1
            vvid = int(input(f"Введіть число {counter} для додавання: "))
            jopka.append(vvid)

        # Сортування (Bubble Sort)
        for i in range(len(jopka)):
            for j in range(len(jopka)):
                if jopka[i] < jopka[j]:
                    jopka[i], jopka[j] = jopka[j], jopka[i]

        print(f"Результат сортування: {jopka}")

def rahuvalnyk():
    stan = True
    while stan:
        a = str(input("Enter any word: "))

        res = len(a)
        print("Length of ur word: ", res)

        for i in a:
         print(i)

         if a == "/stop":
           stan = False
           print("Program ended")
           break
def calc():
    print("Введіть операцію(+ - * /): ")
    x1 = input()
    if x1 == "/stop":
        print("Завершення...")
        exit()
    print("Введіть перше число: ")
    x2 = float(input())
    print("Введіть друге число: ")
    x3 = float(input())
    if x1 == "+":
     print(f"Результат: {x2 + x3}")
    elif x1 == "-":
     print(f"Результат: {x2 - x3}")
    elif x1 == "*":
     print(f"Результат: {x2 * x3}")
    elif x1 == "/":
     print(f"Результат: {x2 / x3}")

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

print("Вітаємо в EasyOS")
#Провідник
stanprocess = True
while stanprocess:
    print("1. Справочник")
    print("2. Калькулятор")
    print("3. Рахувальник")
    print("4. Сортировка")


    maininput = (input("Оберіть програму: "))
#Виконувач
    if maininput == "2": # ВИПРАВЛЕНО: додано лапки
        print("===============")
        calc()
        print("===============")
    elif maininput == "1": # ВИПРАВЛЕНО: додано лапки
        print("---------------")
        print("EasyOS Справочник")
        print("Легка OC для повсякденого користування, командування виконуєтсья через термінал(Linux like)")
        print("Щоб вийти з програми слід написати /stop")
        print("EasyOS v/1 ALPHA(без валідації)")
        print(f"пасхалка = ввести в консоль: єбу діток")
        print("---------------")
    elif maininput == "3": # ВИПРАВЛЕНО: додано лапки
        print("===============")
        rahuvalnyk()
        print("===============")
    elif maininput == "єбу діток":
         open_media()
    elif maininput == "4": # ВИПРАВЛЕНО: додано лапки
        print("===============")
        sortirovka()
        print("===============")