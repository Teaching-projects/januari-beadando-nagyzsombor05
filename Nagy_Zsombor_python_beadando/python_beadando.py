#szorzasgyakprlo_1-10ig

import random

list = []

def osszeadas():
    a = random.randint(0,100)
    b = random.randint(0,100)

    bemenet=input("mennyi "+str(a)+"+"+str(b)+"?")
    while (not bemenet):
        bemenet=input("mennyi "+str(a)+"+"+str(b)+"?")
    bemenet=int(bemenet)

    if bemenet ==a+b:
        print("eltaláltad")
        list.append(1)
    else: 
        print("nem találtad el")
        list.append(0)


def kivonas():
    a = random.randint(0,200)
    b = random.randint(0,100)
    
    bemenet=input("mennyi "+str(a)+"-"+str(b)+"?")
    while (not bemenet):
        bemenet=input("mennyi "+str(a)+"-"+str(b)+"?")
    bemenet=int(bemenet)



    if bemenet ==a-b:
        print("eltaláltad")
        list.append(1)
    else: 
        print("nem találtad el")
        list.append(0)


def szorzas():
    a = random.randint(0,10)
    b = random.randint(0,10)

    bemenet=input("mennyi "+str(a)+"*"+str(b)+"?")
    while (not bemenet):
        bemenet=input("mennyi "+str(a)+"*"+str(b)+"?")
    bemenet=int(bemenet)

    if bemenet ==a*b:
        print("eltaláltad")
        list.append(1)
    else: 
        print("nem találtad el")
        list.append(0)



def osztas():
    a = random.randint(10,100)
    b = random.randint(1,10)

    bemenet=input("mennyi "+str(a)+"/"+str(b)+"?")
    while (not bemenet):
        bemenet=input("mennyi "+str(a)+"/"+str(b)+"?")
    bemenet=int(bemenet)

    if bemenet ==int(round(a/b,0)):
        print("eltaláltad")
        list.append(1)
    else: 
        print("nem találtad el")
        list.append(0)



for i in range(10):
    melyik_legyen=random.randint(1,4)
    if(melyik_legyen == 1 ):
        osszeadas()
    elif(melyik_legyen == 2 ):
        kivonas()
    elif(melyik_legyen == 3 ):
        szorzas()
    else:
        osztas()
with open('result.txt', 'w') as f:
    for i in range(len(list)):
        if(list[i]==1):
            f.write('talalt; ')
        else:
            f.write("nem talalt; ")
