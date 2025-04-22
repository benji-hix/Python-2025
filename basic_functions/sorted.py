monsters = ['Nu Udra', 'Doshaguma', 'Jin Dahaad', 'Chatacabra', 'Arkveld', 'Uth Duna', 'Rey Dau']

# sorted_mons = sorted(monsters)

# print(sorted_mons)

reverse_mons = sorted(monsters, reverse=True)

print(reverse_mons)

threat_level = [
    {'name' : 'Rey Dau', 'threat' : 4},
    {'name' : 'Doshaguma', 'threat' : 3},
    {'name' : 'Gore Magala', 'threat' : 5},
    {'name' : 'Lagiacrus', 'threat' : 4},
    {'name' : 'Gigginox', 'threat' : 3},
    {'name' : 'Dire Miralis', 'threat' : 7},
    {'name' : 'Shagaru Magala', 'threat' : 6},
    {'name' : 'Lagombi', 'threat' : 1}
]

sorted_mons = sorted(threat_level, key=lambda monster: monster['threat'])
print(sorted_mons)