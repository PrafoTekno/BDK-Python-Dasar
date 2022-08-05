
print ("\nContinue dan Pass\n")

index = int (input ("Masukan index : "))

print ("\n")

for s in range (index):
    
    if s == 4:
        continue #berfungsi untuk melompati looping 
        #print ("Mantap")
    elif s == 7:
        pass #berfungsi sebagai dummy

    print (f"Halo bang ke {s}")

print ("\nSelesai")

print ("\n")