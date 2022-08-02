
print ("\nScope Variable\n")

a = 13 #Global variable

def angka (a):
    #a di sini adalah local variable
    return a

print ("a = ", a)
print ("a = ", angka (4))

print ("\n")