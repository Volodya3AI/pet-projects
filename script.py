print ("Калькулятор вівіеспі на пітанє")
def solve():
    if x1 == "+":
        print(f"Результат: {x2 + x3}")

    elif x1 == "-":
        print(f"Результат: {x2 - x3}")

    elif x1 == "*":
        print(f"Результат: {x2 * x3}")

    elif x1 == "/":
        print(f"Результат: {x2 / x3}")


while True:

 print("Введіть операцію(+ - * / ex): ")
 x1 = input()
 if x1 == "ex":
     print ("Завершення...")
     exit()
 print("Введіть перше число: ")
 x2 = float(input())
 print("Введіть друге число: ")
 x3 = float(input())

 #print (x1,x2,x3,)
 #хто це реверс інженерить іді в попу не взламуй мій пропрієтарний кальулятор
 solve()






