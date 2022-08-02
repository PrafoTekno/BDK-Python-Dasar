
print ("\nOperator Bitwise\n")

a = 5
b = 13

print ("====== AND ======\n")

hasil = a & b

print (format (a,'08b'), " | nilai : ", a)
print (format (b,'08b'), " | nilai : ", b)
print ("---------------- Hasil")
print (format (hasil, '08b'), " | nilai : ", hasil)

print ("\n====== OR ======\n")

hasil = a | b

print (format (a,'08b'), " | nilai : ", a)
print (format (b,'08b'), " | nilai : ", b)
print ("---------------- Hasil")
print (format (hasil, '08b'), " | nilai : ", hasil)

print ("\n====== XOR ======\n")

hasil = a ^ b

print (format (a,'08b'), " | nilai : ", a)
print (format (b,'08b'), " | nilai : ", b)
print ("---------------- Hasil")
print (format (hasil, '08b'), " | nilai : ", hasil)

print ("\n====== SHIFT RIGHT ======\n")

hasil = a >> 1

print (format (a,'08b'), " | nilai : ", a)
print ("---------------- Hasil")
print (format (hasil, '08b'), " | nilai : ", hasil)

print ("\n====== SHIFT LEFT ======\n")

hasil = a << 1

print (format (a,'08b'), " | nilai : ", a)
print ("---------------- Hasil")
print (format (hasil, '08b'), " | nilai : ", hasil)


print ("\n")
