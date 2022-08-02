
print ("\nRentang Bil.Bulat\n")

# x < -2 atau x > 4

x = int (input ("Masukan nilai x | x < -2 || x > 4 : "))
hasil = (x < -2) or (x > 4)
print ("Nilai x = ", x, " adalah ", hasil)

# -2 < x < 4

x = int (input ("\nMasukan nilai x | -2 < x < 4 : "))
hasil = (x > -2) and (x < 4)
print ("Nilai x = ", x, " adalah ", hasil)

# 0 < x < 5 atau 8 < x < 11

x = int (input ("\nMasukan nilai x | 0 < x < 5 || 8 < x < 11 : "))
kondisi1 = (x > 0) and (x < 5)
kondisi2 = (x > 8) and (x < 11)
hasil = kondisi1 or kondisi2
print ("Nilai x = ", x, " adalah ", hasil)

# x < 0 atau 5 < x < 8 atau x > 11

x = int (input ("\nMasukan nilai x | x < 0 || 5 < x < 8 || x > 11 : "))
kondisi1 = x < 0
kondisi2 = (x > 5) and (x < 8)
kondisi3 = x > 11 
hasil = kondisi1 or kondisi2 or kondisi3
print ("Nilai x = ", x, " adalah ", hasil)

print ("\n")