
print ("\n*args pada Fungsi\n")

# Fungsi biasa

def orang (nama, tinggi, berat) :
    print (f"{nama} tingginya {tinggi} dan beratnya {berat}")

orang ("Santo", 180, 67)

def orang (list_data) :

    data = list_data.copy ()
    nama = data[0]
    tinggi = data [1]
    berat = data [2]
    print (f"{nama} tingginya {tinggi} dan beratnya {berat}")

orang (["Udin", 170, 50])

# fungsi dengan *args

def orang (*args) :
    nama = args[0]
    tinggi = args [1]
    berat = args [2]
    print (f"{nama} tingginya {tinggi} dan beratnya {berat}")

orang ("Joni", 176, 40)

# Studi kasus

def perkalian (*angka) :
    nilai = 1
    for x in angka :
        hasil = x * nilai
        nilai = hasil
    return hasil

jawab = perkalian (2,3,4,5,7,8,10)

print (f"Jawabannya adalah : {jawab}")

print ("\n")