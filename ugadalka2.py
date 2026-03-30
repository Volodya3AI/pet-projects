import random
print("Обери складність гри")
difficult = int(input("1. Легко 2. Середньо 3. Екстрім 4. Власноруч  "))
if difficult == 1:
    difficult = 10
elif difficult == 2:
    difficult = 50
elif difficult == 3:
    difficult = 100
if difficult == 4:
    difficult = int(input("Напиши ДО скількох: "))
a = 1

print(f"Вгадай число в проміжку від {a} до {difficult}")
number = random.randint(1,difficult)
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