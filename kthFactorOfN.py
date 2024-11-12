import math
def findFactors(n):
    listOfFactors = []
    limit = math.ceil(math.sqrt(n))
    for i in range(1, limit):
        if n % i == 0:
            listOfFactors.append(i)
            listOfFactors.append(int((n / i)))
    return(sorted(listOfFactors))

def findKthFactor(n, k):
    factors = findFactors(n)
    if len(factors) <= k-1:
        return -1
    else:
        return factors[k-1]

print(findKthFactor(12, 3))