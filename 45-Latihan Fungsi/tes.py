
print ("\nMembuat Kotak\n")

# Bahan yang dibutuhkan

def Tampil_Kotak (p = 1, l = 1) :
    
    print ("Ini dia kotak mu : \n")

    for y in range (l) :
        print ("# " * p)

def Luas_Kotak (p, l) :
    return p * l

def Keliling_Kotak (p, l) :
    return 2 * p + 2 * l

# Eksekusi

def Eksekusi () :

    panjang = int (input ("Masukan panjang (bilbul) : "))
    lebar = int (input ("Masukan lebar (bilbul : "))

    print ("\n")

    Tampil_Kotak (panjang, lebar)

    print (f"\nLuas kotak adalah : {Luas_Kotak (panjang, lebar)}")
    print (f"Keliling kotak adalah : {Keliling_Kotak (panjang, lebar)}")


# Looping

while True :

    Eksekusi ()

    tanya = input (f"\nLanjutkah ? (y/n) : ")

    if tanya == 'n' :
        print ("\nTerima kasih, Sampai Jumpa") 
        break
    
    print ("\n")

print ("\n")