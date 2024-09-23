p1= int(input("Preço do primeiro produto: "))
p2= int(input("Preço do segundo produto: "))
p3= int(input("Preço do terceiro produto: "))

if p1<p2 and p1<p3:
    print(f"o produto mais em conta é o primeiro inserido: R${p1},00")
elif p2<p1 and p2<p3:
    print(f"o produto mais em conta é o segundo produto inserido: R${p2},00")
elif p3<p1 and p3<p2:
    print(f"o produto mais em conta é o terceiro produto inserido: R${p3},00")
elif p1==p2 and p1<p3 and p2<p3:
    p11= "primeiro"
    p22= "segundo"
    print(f"dois produtos têm valores iguais e são os mais em conta: o {p11}: R${p1},00 e o {p22}: R${p2},00") 
elif  p1==p3  and p1<p2 and p3<p2:
    p11= "primeiro"
    p33="terceiro"
    print(f"dois produtos têm valores iguais e são os mais em conta: o {p11}: R${p1},00 e o {p33}: R${p3},00")
elif p2==p3 and p2<p1 and p3<p1:
    p22="segundo"
    p33="terceiro"
    print(f"dois produtos têm valores iguais e são os mais em conta: o {p22}: R${p2},00 e o {p33}: R${p3},00")
else:
    print("ambos tem o mesmo valor")
