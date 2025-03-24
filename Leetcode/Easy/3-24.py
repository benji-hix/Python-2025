def kItemsWithMaximumSum(numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
    if numOnes >= k: return k
    maximum = 0
    while k > 0:
        if numOnes > 0:
            maximum += 1
            k -= 1
            numOnes -= 1
        elif numZeros > 0:
            k -= 1
            numZeros -=1
        else:
            maximum -= k
            break
    return maximum

print(kItemsWithMaximumSum(2, 2, 2, 6))