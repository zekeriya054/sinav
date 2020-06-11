class Sinav:
    def __init__(self):
        self.sinav_kodu=''
        self.sinav_adi=''
        self.sinav_tarihi=''
        self.sinav_saati=''
        self.derece=-1
        self.renk=0

class Ogrenci:
    def __init__(self):
        self.numara=''
        self.ad_soyad=''
        self.sinif=''
        self.sinavlar=[]

class SinavProgrami:

    #sınavları oluştur
    sinavlar=[Sinav() for i in range(6)]
    sinavlar[0].sinav_kodu='mat'
    sinavlar[1].sinav_kodu='fiz'
    sinavlar[2].sinav_kodu='kim'
    sinavlar[3].sinav_kodu='biy'
    sinavlar[4].sinav_kodu='tar'
    sinavlar[5].sinav_kodu='coğ'

    #öğrencileri oluştur
    ogrenciler=[Ogrenci() for i in range(4)]
    ogrenciler[0].sinavlar=['mat','fiz','tar']
    ogrenciler[1].sinavlar=['kim','tar','coğ']
    ogrenciler[2].sinavlar=['biy','mat']
    ogrenciler[3].sinavlar=['fiz','tar','mat']

    # komşuluk matrisi oluşturma
    tum_sinavlar=[sinav.sinav_kodu for sinav in sinavlar]
    renkler=[0]*len(sinavlar)
    k_matrisi = [[0] * 6 for i in range(len(sinavlar))]
    for i,sinav in enumerate(sinavlar):
        for j,ogrenci in enumerate(ogrenciler):
            try :
                if sinav.sinav_kodu in ogrenci.sinavlar:
                    for s in ogrenci.sinavlar:
                        if s!=sinav.sinav_kodu:
                            x=tum_sinavlar.index(s)
                            k_matrisi[i][x]=1
            except :
                hata=''
    for i in k_matrisi:
        print(i)         
    
    #matris dereceleri bulunuyor

    derece=[k.count(1) for j,k in enumerate(k_matrisi)]
    print(derece)

    # derslere renk ataması yapılıyor
    renk=1
    for i in range(len(sinavlar)):
        indis=0
        for j in range(i+1,len(sinavlar)):
            if derece[j]>derece[i]:
                indis=j
        renkler[indis]=renk
        sinavlar[indis].renk=renk
        derece[indis]=-1
        #print(derece)
        for n,komsu in enumerate(k_matrisi[indis]):
            if komsu==0:
                if renkler[n]==0:
                    renkler[n]=renk
                    sinavlar[n].renk=renk
        if indis!=0 :
            renk=renk+1
    print(renkler)
    renklerkume=set(renkler)
    print(renklerkume)

    for i in sinavlar:
        print(i.renk)

    

