
print ("\nOperator Assignment\n")

# Operasi aritmatika

a = 6

print ("Nilai a = ", a)
a += 1
print ("Nilai a = ", a)
a -= 3
print ("Nilai a = ", a)
a *= 5
print ("Nilai a = ", a)
a /= 2
print ("Nilai a = ", a)
a %= 8
print ("Nilai a = ", a)
a **= 2
print ("Nilai a = ", a)
a //= 9
print ("Nilai a = ", a)

# Operasi bitwise

b = True
print ("\nNilai b = ", b)
b &= True
print ("Nilai b = ", b)
b |= False
print ("Nilai b = ", b)
b ^= True
print ("Nilai b = ", b)
b = 0b1010
print (format (b, '08b'), " = ", b)
b <<= 3
print (format (b, '08b'), " = ", b)
b >>= 1
print (format (b, '08b'), " = ", b)

print ("")