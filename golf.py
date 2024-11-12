distance = int(input())
copyOfDistance = distance
numberOfStrokes = input()
distanceOfEachClub = []
n = 0

'''
1. subtract each of the club distances from the total distance
2. find factors of said distance using modulus operator
    3. if none are found, subtract each of the club distances from the total distance again 
    4. repeat until factors are found
5. compare each answer with the current answer & if the answer uses less swings - store as answer
'''

for i in range(numberOfStrokes):
    distanceOfEachClub.append(int(input()))
    

for j in distanceOfEachClub:
    if distance % j == 0:
        possibleAnswer = distance // j 
        if possibleAnswer > n:
            n = possibleAnswer

for n 


if n == 0:
    print("Roberta acknowledges defeat")
else:
    print(f"Roberta wins in {n} strokes")