
print ("\nMulti Keys and Nesting Dictionary\n")

import datetime

agent1 = {

    'nama' : "Naruto Uzumaki",
    'code' : 6791,
    'rank' : "Chunin",
    'lahir' : datetime.datetime (2000,10,4)

}

agent2 = {

    'nama' : "Sasuke Uciha",
    'code' : 4588,
    'rank' : "Chunin",
    'lahir' : datetime.datetime (2000,8,5)

}

agent3 = {

    'nama' : "Sakura Haruno",
    'code' : 3328,
    'rank' : "Jonnin",
    'lahir' : datetime.datetime (2000,1,12)

}

Agent_Agent = {

    'AG001' : agent1,
    'AG002' : agent2,
    'AG003' : agent3 

}

print (f"{'KEY':<6} {'NAMA':<19} {'CODE':<4} {'RANK':<5} {'LAHIR':<13}\n")
print (50 * "=" + "\n")

for agt in Agent_Agent :

    KEY = agt

    NAMA = Agent_Agent [KEY]['nama']
    CODE = Agent_Agent [KEY]['code']
    RANK = Agent_Agent [KEY]['rank']
    LAHIR = Agent_Agent [KEY]['lahir'].strftime ("%x")

    print (f"{KEY:<6} {NAMA:<19} {CODE:<4} {RANK:<5} {LAHIR:<13}\n")



print ("\n")