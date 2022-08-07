
print ("\nCopy and Pop Dictionary\n")

mobil = {

    'av' : "Avanza hitam",
    'mr' : "Mercy silver",
    'tl' : "Tesla merah"

}

car = mobil.copy ()

print (f"Car : \n{car}\n")
print (f"Mobil : \n{mobil}")

mobil["av"] = "Avanza putih"

print ("\n")

print (f"Car : \n{car}\n")
print (f"Mobil : \n{mobil}")

# pop (ambil data) dictionary

tesla = mobil.pop ("tl")

print ("\n")

print (f"Data : {tesla}")
print (f"Mobil : \n{mobil}")

# popitem (ambil data yang terakhir aja)

data = mobil.popitem ()

print ("\n")

print (f"Data : {data}")
print (f"Mobil : \n {mobil}")

print ("\n")