dersler=['mat','fiz','kim','biy','tar','coğ']
ogrenciler=['ali','veli','bade','yusuf']
ogrenci_sinavlari=[
    ['mat','fiz','tar'],
    ['kim','tar','coğ'],
    ['biy','mat'],
    ['fiz','tar','mat'],
]
renkler=[0]*len(dersler)
k_matrisi = [[0] * len(dersler) for i in range(len(dersler))]
for i,ders in enumerate(dersler):
    for j,sinavlar in enumerate(ogrenci_sinavlari):

        try :
            
            if ders in sinavlar:
                for sinav in sinavlar:
                    if sinav!=ders:
                        x=dersler.index(sinav)
                        k_matrisi[i][x]=1
                        
        except :
            hata=''
            
for i in k_matrisi:
    print(i);      
derece=[k.count(1) for j,k in enumerate(k_matrisi)]
print(derece)
renk=1
for i in range(len(dersler)):
    indis=0
    for j in range(i+1,len(dersler)):
        if derece[j]>derece[i]:
            indis=j
    renkler[indis]=renk
    derece[indis]=-1
    print(derece)
    for n,m in enumerate(k_matrisi[indis]):
        if m==0:
            if renkler[n]==0:
                renkler[n]=renk
    renk=renk+1
print(renkler)
renklerkume=set(renkler)
print(renklerkume)

  

    
    
    

