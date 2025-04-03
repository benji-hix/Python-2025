"""Length of Last Word"""

def length_of_last_word(s: str) -> int:
    word_list = s.split()
    return len(word_list[-1])

print(length_of_last_word('yes no maybe'))