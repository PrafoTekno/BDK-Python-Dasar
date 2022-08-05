
print ("\nNested Copy List\n")

data_1 = [1,2]
data_2 = [3,4]
data_3 = [5,6]

data_biasa = [1,2,3,4,5,6]
data_2D = [data_1, data_2, data_3]

print (f"Data biasa : {data_biasa}")
print (f"Data 2D : {data_2D}\n")

print (5*"-" + " Lapak " + 5*"-" + "\n")

buah_1 = ["apel", 28, "merah"]
buah_2 = ["jeruk", 12, "oranye"]
buah_3 = ["pisang", 20, "kuning"]

lapak = [buah_1, buah_2, buah_3]

for buah in lapak:

    print (f"Buah  : {buah[0]}")
    print (f"Berat : {buah[1]} kg")
    print (f"Warna : {buah[2]}\n")

print ("\n")