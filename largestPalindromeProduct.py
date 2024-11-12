def findLargestPalindrome():
    answer = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            numString = str(product)
            if numString[::-1] == numString:
                answer = max(answer, int(numString))

    return answer

print(findLargestPalindrome())