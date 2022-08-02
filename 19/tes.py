
print ("\nOperasi Komperasi\n")

#Komaparasi atau membandingkan akan selalu bernilai boolean (True/False)

x = 9
y = 3

hasil = x > y
print (x, " >\t\t", y, " | ", hasil)
hasil = x >= y
print (x, " >=\t\t", y, " | ", hasil)
hasil = x < y
print (x, " <\t\t", y, " | ", hasil)
hasil = x <= y
print (x, " <=\t\t", y, " | ", hasil)
hasil = x == y
print (x, " ==\t\t", y, " | ", hasil)
hasil = x != y
print (x, " !=\t\t", y, " | ", hasil)

print ("\n")

#Pembanding id (address)

y = x = 3 #di python nilai nya sama maka addressnya sama

print ("x = ", x, " id = ", hex (id (x)))
print ("y = ", y, " id = ", hex (id (y)))

print ("\n")

hasil = x is y 
print (x, " is\t\t", y, " | ", hasil)
hasil = x is not y
print (x, " is not\t", y, " | ", hasil)

print ("\n")