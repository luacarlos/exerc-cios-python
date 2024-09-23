while True:
    print('--------------------------------------')
    n=1
    total= 0
    while True:
        p= float(input(f"valor do produto {n}: "))
        n= n+1 
        total= total+ p
        if p==0:
            break
    print (f"valor final  da compra:: {total}")
    break

pg= input("pagamento: ")
troco= float(pg) - float(total)
if troco>=0:
    print(f' troco {troco}')
