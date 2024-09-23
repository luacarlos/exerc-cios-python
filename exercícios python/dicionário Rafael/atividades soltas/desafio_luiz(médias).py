medias= {}

for i in range(4): 
    medias[f"nota {i+1}"]= float(input(f"digite a {i+1}º nota: "))
nova_media=0
for m in medias: 
    nova_media+=(medias[m])

print(f"medias= {nova_media/4}")        