
print ("\nDeep Copy Nested List\n")

angka_0 = [1,2]
angka_1 = [3,4]

angka_list = [angka_0, angka_1]
angka_list_copy = angka_list.copy ()

print (f"List angka : {angka_list}")
print (f"List angka_copy : {angka_list_copy}\n")

print (f"Address list angka : {hex (id (angka_list))}")
print (f"Address list copy : {hex (id (angka_list_copy))}")

print (7*"-" + " Modif " + 7*"-" + "\n")

# mengganti anggota pada angka_list

angka_list[0][1] = 9
print (f"List angka : {angka_list}")
print (f"List angka copy : {angka_list_copy}\n\n")

print (7*"=" + " Deepcopy " + 7*"=" + "\n")

from copy import deepcopy

angka_list_copy = deepcopy (angka_list)

print (f"List angka : {angka_list}")
print (f"List angka_copy : {angka_list_copy}\n")

print (f"Address list angka : {hex (id (angka_list))}")
print (f"Address list copy : {hex (id (angka_list_copy))}\n")

print (7*"-" + " Modif " + 7*"-" + "\n")

# mengganti anggota pada angka_list

angka_list[0][1] = 13
print (f"List angka : {angka_list}")
print (f"List angka copy : {angka_list_copy}")

print ("\n")