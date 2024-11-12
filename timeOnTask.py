T = int(input()) # number of minutes given to complete the given tasks
C = int(input()) # number of chores given to you
numberOfChoresToDo = 0

'''
can create a dictionary of the number of minutes a chore takes and the number chores that take x amount of minutes
    to do this:
        1. for the number of times C has indicated, take in user input
        2. check if the number is already in the dictionary, if not 
            3. create new key and assign value of 1
            ELSE
            4. add one to the value of the existing key
        5. once user input is done, while T >= 0:
            6. iterate through dictionary and look at the first index to subtract from the 
then will take the task with the lowest amount of minutes each time
'''

timeNeededForChores = {}
for i in range(C): # collecting user input
    choreMinutes = input()
    if choreMinutes in timeNeededForChores:
        timeNeededForChores[choreMinutes] += 1
    else:
        timeNeededForChores[choreMinutes] = 1

timeForChores = dict(sorted(timeNeededForChores.items()))

loop = True
while loop:
    for k, v in timeForChores.items():
        if loop == False:
            break
        else:
            # k is a str that states how much time the chore would take
            # v is an int that states how many of these chores that must be done
            for j in range(0, v):
                if T - int(k) >= 0:
                    T -= int(k)
                    numberOfChoresToDo += 1
                else: 
                    print(numberOfChoresToDo)
                    loop = False
                    break