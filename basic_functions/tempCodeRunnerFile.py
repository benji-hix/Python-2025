monsters = ['Nu Udra', 'Doshaguma', 'Jin Dahaad', 'Chatacabra', 'Arkveld', 'Uth Duna', 'Rey Dau']

def two_words(name: str) -> bool:
    return " " in name

filtered = filter(two_words, monsters)

print(list(filtered))
print(filtered)