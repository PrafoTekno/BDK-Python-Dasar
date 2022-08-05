
print ("\nKalkulator Sederhana\n")

x = float (input ("Masukan angka pertama : "))
y = float (input ("Masukan angka kedua : "))

operasi = input ("Masukan tanda operasi (+,-,*,/) : ")

print ("\n")

if operasi == '+':
    print (f"{x} + {y} = {(x + y):.3f}")

elif operasi == '-':
    print (f"{x} - {y} = {(x - y):.3f}")

elif operasi == '*':
    print (f"{x} * {y} = {(x * y):.3f}")

elif operasi == '/':
    print (f"{x} / {y} = {(x / y):.3f}")

else:
    print (f"Tanda operasi yang dimasukan tidak ada dalam opsi")

print ("\nSampai jumpa\n")

print ("\n")