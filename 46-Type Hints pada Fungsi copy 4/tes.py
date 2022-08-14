
print ("\nType Hints pada Fungsi\n")

"""
Studi kasus

def sesuatu (x) :
    jawab = x ** 2
    print (f"inputnya adalah {jawab}")

sesuatu (4)
sesuatu ("Udin")
sesuatu (False)
"""

def pangkat (x : int) -> int : 
    # x : int (tipe input adalah int)
    # -> int (me return hasil bertipe int)

    hasil = x **2
    return hasil

nilai = pangkat (10)
print (nilai)

print ("\n")