p= 1
s=2
t=3 
n= int(input("digite o número: "))

while True:

    verdadeiro= p*s*t

    p+=1
    s+=1
    t+=1

    if verdadeiro==n:
        print("deu certo")
        break
    elif n<verdadeiro:
        print("deu errado")
        break