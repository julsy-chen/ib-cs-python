import math

answer = [1, 1]

def findNumWithMostFactors(num):
    factors = []
    for j in range(1, math.floor(math.sqrt(num))):
        if num % i == 0: # factor found
            factors.append(i)
            factors.append(num / i)
    if answer[1] < len(factors): # new answer
        answer[0] = num
        answer[1] = len(factors)

N = int(input())
for i in range(1, N):
    findNumWithMostFactors(i)

print(f"{answer[0]} is the number with the most factors of {answer[1]}")

