
print ("\nFungsi dengan Deafult Argument\n")

def kata (a = "Semangat") :
    print (f"Kata itu adalah {a}")

kata ()
kata ("Hebat")

def kotak (x = 2, y = 2) :
    return x * y

print (f"\nLuas kotak = {kotak (4,6)}")
print (f"Luas kotak = {kotak ()}")

print ("\n")