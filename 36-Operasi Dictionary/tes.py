
print ("\nOperasi Dictionary\n")

agent = {

    'al' : "Ali ghozali",
    'ud' : "Udin ganteng",
    'jo' : "Jono hebat",
    'sa' : "Sarah swasti"

}

# Panjang dictionary

PANJANG_DICT = len (agent)
print (f"Panjang dictionary = {PANJANG_DICT}\n")

# Mengecek key dictionary ada atau tidak

KEY = 'al'
CHEK_KEY = KEY in agent
print (f"Apakah ada key '{KEY}' pada agent : {CHEK_KEY}\n")

# Mengakses value (read) dengan get 

print (agent['jo'])
print (agent.get ('ud'))
print (agent.get ('ol', "Key tidak ditemukan") + "\n")

# Mengupdate data 

agent['jo'] = "Joni hebat"
print (f"{agent}\n")
agent.update ({'ud' : "Ujang keren"})
print (f"{agent}\n")
agent.update ({'do' : "Dodo kece"})
print (f"{agent}")

# Menghapus data

del agent ['do']
print (f"\n{agent}")

print ("\n")