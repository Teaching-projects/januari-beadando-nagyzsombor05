#beadandó 
#nem végleges változat csak a beadandó irányát mutatja
"""
a program célja az alap matematikai műveletek gyakorlása(szorzás,osztás,összeadás,kivonás)

"""



import random
def osszeadas():
    a = random.randint(100)
    b = random.randint(100)

    bemenet=int(input("mennyi",a,"+",b,"? "))

    if bemenet ==a+b:
        print("eltaláltad")
    else: print("nem találtad el")


def kivonas():
    a = random.randint(200)
    b = random.randint(100)
    
    bemenet=int(input("mennyi",a,"-",b,"? "))
     
    if bemenet ==a-b:
        print("eltaláltad")
    else: print("nem találtad el")


def szorzas():
    a = random.randint(10)
    b = random.randint(10)

    bemenet=int(input("mennyi",a,"*",b,"? "))

    if bemenet ==a*b:
        print("eltaláltad")
    else: print("nem találtad el")



def osztas():
    a = random.randint(10,100)
    b = random.randint(10)

    bemenet=int(input("mennyi",a,"/",b,"? "))

    if bemenet ==int(round(a/b,0)):
        print("eltaláltad")
    else: print("nem találtad el")



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
