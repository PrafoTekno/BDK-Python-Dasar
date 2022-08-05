
print ("\nCopy List\n")

buah = ["anggur", "jeruk", "mangga", "kelapa"]
buah_new = buah

print (f"Buah : {buah}")
print (f"Buah new : {buah_new}\n")

# mengganti anggota pada buah
buah[3] = "apel"

print (f"Buah : {buah}")
print (f"Buah new : {buah_new}\n")

print (f"Alamat Buah     : {id (buah)}")
print (f"Alamat Buah new : {id (buah_new)}")
# list buah dan buah_new memiliki address yang sama

buah_new = buah.copy ()

print (f"\nBuah : {buah}")
print (f"Buah new : {buah_new}\n")

print (f"\nAlamat Buah     : {id (buah)}")
print (f"Alamat Buah new : {id (buah_new)}")
# list buah dan buah new memiliki address yang berbeda

# insert "pepaya" di list buah
buah.insert (2, "pepaya")
print (f"\nBuah : {buah}")
print (f"Buah new : {buah_new}\n")

print ("\n")
