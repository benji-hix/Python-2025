def minOperations(s: str) -> int:
    # count = 0
    # s_list = list(s)
    # index = 0
    # while index < len(s_list) - 1:
    #     if s_list[index] == s_list[index + 1]:
    #         count+= 1
    #         s_list[index+1] = "0" if s_list[index] == "1" else "1"
    #     index += 1
    # return count
# First attempt didn't because it was calculating the min number of operations
# strictly for a linear, left-to right solution where only digits
# to the right could be changed.
    count1 = 0
    count2 = 0
    s_list = list(s)
    for index, digit in enumerate(s_list):
        if (index % 2 == 0 and digit != "1") or (index % 2 != 0 and digit != "0"):
            count1 += 1
        if (index % 2 == 0 and digit != "0") or (index % 2 != 0 and digit != "1"):
            count2 += 1
    return min(count1, count2)
        
# Improvements: include a guard clause for single-digit strings

test = "111100101"

print(minOperations(test))