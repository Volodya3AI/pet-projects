import keyboard
import time

def render():
    print("\n" * 100)
    print(f"Ваш рахунок :{score}")
    for i in mapa:
     print(*i)
def check():
    if mapa[x][y] == "*":
        print ("Не можна проходити крізь стіни")
        mapa[x][y] = "*"
score = 0


print("Використовуй стрілки для руху")

mapa = [
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # рядок 0
    ["*", " ", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "C", "*"],  # рядок 1
    ["*", " ", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],  # рядок 2
    ["*", " ", "*", " ", " ", " ", "*", " ", " ", " ", "*", " ", " ", " ", "*"],  # рядок 3
    ["*", " ", " ", " ", "*", "*", "*", " ", " ", " ", "*", " ", " ", " ", "*"],  # рядок 4
    ["*", " ", " ", " ", "*", " ", "C", " ", " ", "*", "*", "*", " ", " ", "*"],  # рядок 5
    ["*", "C", " ", " ", "*", " ", " ", " ", " ", " ", "*", "C", " ", " ", "*"],  # рядок 6
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]  # рядок 7
    # ел. 0   1    2    3    4    5    6    7    8    9    10   11   12   13   14
]

x = 1
y = 1

mapa[x][y] = "@"




while True:
    moved = False
    if keyboard.is_pressed("up"):
        mapa[x][y] = " "
        x -= 1
        moved = True
        if mapa[x][y] == "*":
            moved = False
            x += 1
    elif keyboard.is_pressed("down"):
        mapa[x][y] = " "
        x += 1
        moved = True
        if mapa[x][y] == "*":
            moved = False
            x -= 1
    elif keyboard.is_pressed("left"):
        mapa[x][y] = " "
        y -= 1
        moved = True
        if mapa[x][y] == "*":
            moved = False
            y += 1
    elif keyboard.is_pressed("right"):
        mapa[x][y] = " "
        y += 1
        moved = True
        if mapa[x][y] == "*":
            moved = False
            y -= 1
    if mapa[x][y] == "C":
        score += 1
    if score == 4: # -----------------рахувати вписувати скільки C(очок) на мапі вручну(можна автоматично здєлать но єта міні абновочка), щоб завершити гру
        print("Ти пройшов гру! Вітаю!")
        break
    #check()
    #if mapa[x][y] == "*":
        #print("Ти не можеш пройти через стіну!")
        #mapa[x][y] = mapa[x][y]
        #moved = False
    if moved:
     mapa[x][y] = "@"
     check()
     render()
     time.sleep(0.1)






