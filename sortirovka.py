jopka = []
vvod = int(input("Введіть кількість чисел для сортування: "))
counter = 0
while vvod > counter:
        counter = counter + 1
        vvid = int(input(f"Веддіть число {counter} для добавлення: "))
        jopka.append(int(vvid))
#print(jopka)
for i in range(len(jopka)):
    for j in range(len(jopka)):
        if jopka[i] < jopka[j]:
            jopka [i], jopka[j] = jopka[j], jopka[i]
print(jopka)