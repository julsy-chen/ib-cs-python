import math

perfectNumbers = []

# finding factors of a number function
def findFactorsOfNum(num):
    factors = []
    for i in range(2, math.floor(math.sqrt(num))):
        if num % i == 0: # we have found a factor
            factors.append(i)
            factors.append(num / i)

    # checking if the factors add up to the number given
    if sum(factors) + 1 == num: # is a perfect number
        perfectNumbers.append(num)

# adding up all the numbers within the perfectNumbers list

for i in range (10000):
    findFactorsOfNum(i)

sumOfPerfectNumbers = sum(perfectNumbers)

print(sumOfPerfectNumbers)