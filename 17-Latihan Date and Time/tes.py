
import datetime as dt

print ("\nLatihan Date and Time\n")

"""
hari_ini = dt.date.today ()
print (f"Hari ini : {hari_ini:%A}, {hari_ini}")

tanggal = dt.date (2000, 5, 12)
print (f"Hari {tanggal:%A}, {tanggal}")
"""

tanggal = int (input ("Masukan tanggal lahir\t: "))
bulan = int (input ("Masukan bulan lahir\t: "))
tahun = int (input ("Masukan tahun lahir\t: "))

lahir_input = dt.date (tahun, bulan, tanggal)
saat_ini = dt.date.today ()
umur = (saat_ini - lahir_input).days // 365 
bulan_sisa = ((saat_ini - lahir_input).days % 365) // 30

print (f"\nTanggal lahirnya adalah {lahir_input}")
print (f"\nHari lahirnya adalah {lahir_input:%A}")
print (f"\nUmur nya saat ini adalah {umur} tahun, {bulan_sisa} bulan")

print ("\n")