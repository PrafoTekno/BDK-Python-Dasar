
print ("\nFungsi dengan Argument\n")

def penjumlahan (a, b) : 
    print (f"{a} + {b} = {a + b:.3f}")

angka1 = float (input (f"Masukan angka pertama : "))
angka2 = float (input (f"Masukan angka kedua : "))

penjumlahan (angka1, angka2)

def sambutan (nama_orang) :
    data = nama_orang.copy ()

    for orang in data :
        print (f"Halo {orang}")

print ("\n")

shinobi = ["Naruto", "Sakura", "Sasuke"]
sambutan (shinobi)

print ("\n")