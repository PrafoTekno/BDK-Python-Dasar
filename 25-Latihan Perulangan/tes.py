
print ("\nSegitiga siku-siku\n")

sisi = 16

print ("Pake For\n")

i = 1

for y in range (sisi):
    print ("x"*i)
    i += 1

print ("\nPake While\n")

i = 1

while True:
    
    print ("x"*i)
    i += 1

    if i > sisi:
        break

print ("\nGanjil only\n")

i = 1

for y in range (sisi):

    if i%2 == 0: #jika genap
        i += 1
        continue
    else : #jika ganjil
        print ("x"*i)
        i += 1

print ("\nGenap only\n")

i = 1

for y in range (sisi):

    if i%2 != 0: #jika ganjil
        i += 1
        continue
    else : #jika genap
        print ("x"*i)
        i += 1

print ("\nSelesai")

print ("\n")