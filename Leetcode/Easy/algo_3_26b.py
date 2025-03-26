"""Longest Common Prefix"""

# Time complexity: O(N*M)
def longest_common_prefix(strs: list[str]) -> str:
    """
    Find the longest common prefix string amongst an array
    of strings.

    Args:
        strs (list[str]): List of strings

    Returns:
        str: The longest common 'prefix' from the list.
    """
    def find_min_length(list):
        min_length = len(list[0])
        for item in list:
            if len(item) < min_length:
                min_length = len(item)
        return min_length
    
    def compare_letter(index, word_list, letter):
        for word in word_list:
            
            if word[index] != letter:
                return False
        return True
    
    end_index = find_min_length(strs)
    compare = strs[0][:end_index]
    output = ''
    for character_index in range(0, end_index):
        if compare_letter(character_index, strs, compare[character_index]):
            output += compare[character_index]
        else: break
    return output

# Optimized Solution
def longest_common_prefix_optimized(words: list[str]) -> str:
    ans=""
    sorted_words = sorted(words)
    print("Sorted:")
    print(sorted_words)
    first=sorted_words[0]
    last=sorted_words[-1]
    for i in range(min(len(first),len(last))):
        if(first[i]!=last[i]):
            return ans
        ans+=first[i]
    return ans 

longest_common_prefix_optimized(['parameter', 'partake', 'partridge', 'parasocial', 'park', 'par'])