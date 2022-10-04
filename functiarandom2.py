import random 
x=round(random.random()*10)
l=[]

for ele in range(x):
    l.append(random.randint(1,6))
    p=l.count(6)
    
print("nr de aruncari = ",x)
print("zarurile au cazut pe fetele= ",l)
if p==0:
    print("Fata nr 6 nu a cazut nici o data")
else:
    print("Fata cu cifra 6 a cazut de",p,"ori")