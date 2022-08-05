
print ("\nOperasi Pada List\n")

angka = [0,2,3,5,1,5,3,5,1,9]
print (f"Angka : {angka}\n")

# Menghitung jumlah suatu anggota pada list

jumlah_angka1 = angka.count (1)
print (f"Jumlah angka 1 : {jumlah_angka1}")

# ambil posisi pada suatu anggota
index_1 = angka.index (1)
print (f"Index angka 1 adalah {index_1}") 

# mengurutkan list 
print (f"\nData sebelumnya : {angka}")
angka.sort ()
print (f"Data setelah disort : {angka}")

nama = ["Jordi", "Bagus", "Asep"]
print (f"\nData sebelumnya : {nama}")
nama.sort ()
print (f"Data setelah disort : {nama}\n")

# mereverse list 
print (f"\nData sebelumnya : {angka}")
angka.reverse ()
print (f"Data setelah direverse : {angka}")


print ("\n")