
print ("\nLooping Dictionary\n")

mobil = {
    'av' : "Avanza hitam",
    'mr' : "Mercy silver",
    'tl' : "Tesla merah"
}

# operator untuk mengambil item/iterables

print ("Key\n")

keys = mobil.keys ()
print (keys)

print ("\n")

for k in mobil.keys ():
    print (mobil.get (k))

print ("\nValue\n")

nilai = mobil.values ()
print (nilai)

print ("\n")

for v in mobil.values ():
    print (v)

print ("\nItems\n")

item = mobil.items ()
print (item)

print ('\n')

for key, value in mobil.items ():
    print (f"{key} : {value}")

print ("\n")