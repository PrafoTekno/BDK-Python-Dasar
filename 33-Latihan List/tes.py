
print ("\n" + 10*"=" + " List Agent " + 10*"=" + "\n")

list_agent = []

while True :

    print (f"----- Data Buku -----\n")

    nama = input ("Masukan nama agent : ")
    kode = input ("Masukan kode agent : ")
    unit = input ("Masukan unit agent : ")

    agent = [nama, kode, unit]

    list_agent.append (agent)

    print (f"\nNo  Nama\t|\tKode\t|\tUnit")

    for nomor, data in enumerate (list_agent) : 
        print (f"{nomor+1}.  {data[0]}\t|\t{data[1]}\t|\t{data[2]}")

    cek = input ("\nLanjut? y/n : ")

    if cek == 'n':
        break
    
    print ("\n")

print ("\nTerima kasih, sampai jumpa")

print ("\n")