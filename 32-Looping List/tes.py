
print ("\nLooping List\n")

buah = ["apel", "mangga", "jeruk", "pisang", "semangka"]
print (f"List buah : {buah}\n")

print (7*"=" + " For Loop " + 7*"=" + "\n")

for s in buah :
    print (f"Buah {s}")

print ("\n" + 4*"=" + " For Loop dan Range " + 4*"=" + "\n")

panjang = len (buah)

for s in range (panjang) :
    print (f"Buah {buah[s]}")

print ("\n" + 6*"=" + " While Loop " + 6*"=" + "\n")

s = 0

while s < panjang :
    print (f"Buah {buah[s]}")
    s += 1 

print ("\n" + 4*"=" + " List Comprehesion " + 4*"=" + "\n")

[print (f"Buah {s}") for s in buah]

print ("\n" + 6*"=" + " Enumerate " + 6*"=" + "\n")
# enumerate digunakan saat kita ingin melooping iterasi, sambil menghitung index

for index, nama in enumerate (buah) :
    print (f"{index}. Buah : {nama}")

print ("\n")