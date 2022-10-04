import random
n=int(input("Dati un  nr:"))
suma=0
suma2=0
nr=[]
for x in range (n):
    i=random.randint(-30,50)
    nr.append(i)
    if i>0:
        suma=suma+i
    elif i<=0:
        suma2=suma2+i

print("Numerele sunt:",nr)
if suma==0:
    print(" EROARE:Nu sunt nr pozitive")
if suma!=0:
    print("Suma numerelor pozitive este:",suma)
if suma2==0:
    print("Nu au fost generate nr. negative.")
if suma2!=0:
    print("Suma numerelor negtive este:",suma2)