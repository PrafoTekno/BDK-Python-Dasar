
print ("\nManipulasi List\n")

mobil = ["Avanza", "Toyota", "Kijang"]
print (f"{mobil}\n")

# mengambil anggota list
print (f"Mobil index ke 0 = {mobil[0]}")
print (f"Mobil index terakhir = {mobil[-1]}\n")

# panjang list
panjang_data = len(mobil)
print (f"Panjang list : {panjang_data}\n")

# mengganti anggota pada list
mobil[2] = "Tesla"
print (f"{mobil}\n")

# insert anggota baru pada list
mobil.insert (2, "Audy") #index, anggota_baru
print (f"{mobil}\n") 

# menambahkan anggota baru di index terakhir
mobil.append ("Ferrary")
print (mobil)

# menambahkan anggota dari list lain
orang = ["Joni", "Udin", "Grido"]
mobil.extend (orang)
print (mobil)

# menghapus anggota pada list
mobil.remove ("Avanza")
print (mobil)

# menghapus anggota terakhir pada list
mobil.pop ()
print (mobil)

print ("\n")