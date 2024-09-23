numeros= [1,2,3,4,5,6,7,8,9]
def par():
    pares= []
    for i in numeros: 
        if i%2==0:
            pares.append(i)
    somaPar= sum(pares)
    return(somaPar)

def impar():
    impares= []
    for i in numeros:
        if i%2!=0:
            impares.append(i)
    somaImpar= sum(impares)
    return (somaImpar)

print(par())
print(impar())