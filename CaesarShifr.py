resultencode = []
resultdecode = []

word_for_encode = input("Введіть слово для шифру: ")
word_for_decode = input("Введіть слово для розшифровки: ")


def encode():
 for el in word_for_encode:
     a = (chr(ord(el)+4))
     #print(a)
     resultencode.append(a)

encode()
print(*resultencode)

def decode():
 for el in word_for_decode:
     a = chr(ord(el) - 4)
     #print(a)
     resultdecode.append(a)

decode()

print(*resultdecode)










