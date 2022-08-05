
print ("\nOperasi Pada String\n")

# Menyambung string (concatenate)

nama_depan = "Udin"
nama_tengah = "Keren"
nama_belakang = "Jainudin"

nama_lengkap = nama_depan + " " + nama_tengah + " " + nama_belakang
print (nama_lengkap)

# Menghitung panjang string 
panjang = len (nama_lengkap)
print ("Panjang = ", panjang)

# Mengecek komponen char atau string di dalam sebuah string
huruf = 'a'
cek = huruf in nama_lengkap
print ("Huruf ", huruf, " ada dalam ", nama_lengkap, " : ", cek)

huruf = 'r'
cek = huruf not in nama_lengkap
print ("Huruf ", huruf, " tidak ada dalam ", nama_lengkap, " : ", cek)

# Mengulang string
print (10 * "ha")

# Indexing 
print ("Index ke 2 dari " + nama_lengkap + " = " + nama_lengkap[2])
print ("Index ke -1 dari " + nama_lengkap + " = " + nama_lengkap[-1])
print ("Index ke 2:5 dari " + nama_lengkap + " = " + nama_lengkap[2:6])
print ("Index ke 0,2,4,6,8,10,12 dari " + nama_lengkap + " = " + nama_lengkap[0:12:2])

# Nilai max-min
print ("Nilai max dari " + nama_belakang + " = " + max (nama_belakang))
print ("Nilai min dari " + nama_belakang + " = " + min (nama_belakang))

# ASCII CODE
karakter = ord ("g")
print ("ASCII CODE dari g = " + str (karakter))
code = 125
print ("Karakter dari 125 = " + chr (code))

# Operator dalam bentuk method 

## mencari banyaknya sebuah karakter
banyak = nama_lengkap.count ("i")
print ("Banyak huruf i pada " + nama_lengkap + " = " + str (banyak))

## merubah semuanya ke upper case
kata = "Halo"
kata = kata.upper ()
print (kata)

## merubah semuanya ke lower case
kata = "KOCAK"
kata = kata.lower ()
print (kata)

## pengecekan isX 
kata = "Bagus"
print ("Kata = " + kata)
cek = kata.islower ()
print ("Cek is lower = " + str (cek))

"""
Catatan :

isalpha () = untuk ngecek semuanya huruf
isalnum () = untuk ngecek semuanya angka dan huruf
isdecimal () = untuk ngecek angka saja
isspace () = untuk ngecek spasi, tab, newline
istitle () = untuk ngecek semua huruf di awal kata adalah upper case

"""

## startswith () dan endwith ()
cek_awal = "Kamu hebat banget".startswith ("Kamu")
print (cek_awal)
cek_akhir = "Kamu hebat banget".startswith ("Banget")
print (cek_akhir)

## join () dan split ()
pisah = ["halo", "apa", "kabar"]
gabung = "-".join (pisah)
print (pisah)
print (gabung)
pisah = "-".split (gabung)
print (pisah)

## alokasi 
kanan = "kata".rjust (12) #geser ke kanan
print (kanan)
kiri = "kata".ljust (10) #geser ke kiri
print (kiri)
tengah = "kata".center (20,"-")
print (tengah)

## strip (kebalikannya)
tengah = tengah.strip ("-")
print ('"' + tengah + '"')

print ("\n")
