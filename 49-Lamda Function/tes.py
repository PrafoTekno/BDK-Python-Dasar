
print ("\nLambda Function\n")

def kuadrat (angka) :
    return angka**2

print (f"Hasil kuadrat = {kuadrat (6)}")

# lambda
# output = lambda argument : perintah

kuadrat = lambda angka : angka ** 2
print (f"Hasil kuadrat = {kuadrat (4)}")

print ("\n")

## kegunaan

# sorting list
 
data_list = [2,4,1,3,2,5,7]
data_list.sort ()
print (f"Sorting list {data_list}")

data_list = ["apel", "jeruk", "pisang", "mangga", "anggur"]
data_list.sort (key=lambda data : len(data))
print (f"Urutan dengan lambda : {(data_list)}")

print ("\n")

# filter 
angka = [4,1,3,2,7,9,1,4,2]

def kondisi (a) :
    return a < 6

angka_baru = list (filter (kondisi, angka))
print (f"angka < 6 dengan def : {angka_baru}")

angka_baru = list (filter (lambda a : a < 6, angka))
print (f"angka < 6 dengan lambda : {angka_baru}")

angka_genap = list (filter (lambda a : a%2 == 0, angka))
print (f"angka genap dengan lambda : {angka_genap}")

print ("\n")

# anonymous function

## currying 

def pangkat (n, r):
    hasil = n ** r
    return hasil

print (f"Pangkat dengan fungsi biasa : {pangkat (6,3)}")

def pangkat (n):
    return lambda angka : angka ** n

pangkat_2 = pangkat (2)
print (f"Pangkat dengan currying (def dan lambda) : {pangkat_2 (7)}")
pangkat_5 = pangkat (5)
print (f"Pangkat dengan currying (def dan lambda) : {pangkat_5 (5)}")
print (f"Pangkat dengan currying (def dan lambda) : {pangkat (4)(7)}")

print ("\n")