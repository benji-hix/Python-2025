"""Python Testing"""

strs = ["dog","racecar","car"]

def find_min_length(list):
    min_length = len(list[0])
    for item in list:
        if len(item) < min_length:
            min_length = len(item)
    return min_length

def compare_letter(index, word_list, letter):
    for word in word_list:
        
        if word[index] != letter or word[index] == None:
            return False
    return True

def compare_words(word_list):
    end_index = find_min_length(word_list)
    print(f'End index: {end_index}')
    compare = word_list[0][:end_index]
    print(f'Compare str: {compare}')
    output = ''
    for character_index in range(0, end_index):
        if compare_letter(character_index, word_list, compare[character_index]):
            output += compare[character_index]
    return output

print(f"The result is: '{compare_words(strs)}'")
