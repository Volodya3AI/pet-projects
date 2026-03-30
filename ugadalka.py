import random
print("Напиши перше число діапазону")
a = int(input())
print("Напиши друге число діапазону")
b = int(input())
print(f"Вгадай число в проміжку від {a} до {b}")
number = random.randint(a,b)
#print(number)
def game():
 stan = True
 while stan:
     c = int(input("Вгадуй: "))
     if c > number: print("менше")
     elif c < number: print("більше")
     if c == number:
         print("Правильно! Ти вгадав")
         stan = False


game()