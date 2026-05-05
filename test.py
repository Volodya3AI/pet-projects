#a = int(input("Enter range FROM: "))
#b = int(input("Enter range TO: ")) + 1

#for i in range(a, b):
    #print (i)
#----------------------

def rahuvalnyk():
    stan = True
    while stan:
        a = str(input("Enter any word: "))

        res = len(a)
        print("Length of ur word: ", res)

        for i in a:
         print(i)

        if a == "stop":
           stan = False
           print("Program ended")
           break


rahuvalnyk()
#----------------------

