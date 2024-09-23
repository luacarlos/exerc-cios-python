lista= [1,1]
ult= 1
pen= 1

for i in range(13):
    result= ult+pen
    pen= ult
    ult= result
    lista.append(result)
print(lista)