
from telnetlib import STATUS


print ("\nFormat String\n")

# string
nama = "Udin"
print (f"Nama : {nama}")

# boolean
status = False
print (f"Status : {status}")

# bilbul
bilbul = 45
print (f"Bilbul : {bilbul:d}")

# ordo ribuan
angka = 500002000
print (f"Angka : {angka:,}")

# bilangan decimal
angka = 567.3456
print (f"Decimal : {angka:.3f}") # format 3 angka belakang koma (.)

# leading zero
angka = 456.78992
print (f"Decimal : {angka:09.2f}")

# min plus
angka = -46.64
print (f"Angka : {angka:-1f}")

# persentase
persen = 0.0057
print (f"Persen : {persen:.1%}")

# operasi aritmatika
banyak_data = 7
jumlah_data = 194
print (f"Mean : {jumlah_data/banyak_data:.2f}")

# format angka lain
angka = 89
print (f"Binary : {bin(angka)}")
print (f"Octal : {oct(angka)}")
print (f"Hex : {hex(angka)}")

print ("\n")