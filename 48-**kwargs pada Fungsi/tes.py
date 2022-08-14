
print ("\n**kwargs pada Fungsi\n")

def orang (nama, tinggi, berat):
    print (f"{nama} memiliki tinggi {tinggi} cm dan berat {berat} kg")

orang ("Sasuke", 178, 56)

def orang (**kwargs):

    nama = kwargs["n"]
    tinggi = kwargs["t"]
    berat = kwargs["b"]
    print (f"{nama} memiliki tinggi {tinggi} cm dan berat {berat} kg")

orang (n = "Udin", t = 173, b = 50)

def mtk (*args, **kwargs):
    
    #penjumlahan
    if kwargs["opsi"] == "tambah":
        nilai = 0
        for i in args:
            nilai = nilai + i
        return nilai

    elif kwargs["opsi"] == "kali":
        nilai = 1
        for i in args:
            hasil = nilai * i
            nilai = hasil
        return hasil    
    
    else : 
        print ("Error : tidak ada input yang tersedia")


jawab = mtk (4,6,2,4,3,7,18,9, opsi = "tambah")
print (jawab)
jawab = mtk (4,6,2,1,5,0,1,9, opsi = "kali")
print (jawab)

print ("\n")