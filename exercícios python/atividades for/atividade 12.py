num = int(input("qual tabuada você deseja (números entre 1 e 10)"))

if num<=1 or num<=10:
    print(f"tabuada do {num}")
    for i in range(1,11):
        mult= num*i
        print(f"{num} X {i}= {mult}")
elif num<0 or num>10: 
    print("tabuada inválida")
    
