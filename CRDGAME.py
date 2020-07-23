
def divideStringIntoIndividualIntegersAndSum(number):
    number = str(number)
    l = len(number)
    newNumber = 0
    for i in range(len(number)):
        newNumber += int(number[i])

    # if newNumber > 9:
    #     return divideStringIntoIndividualIntegersAndSum(newNumber)
    return newNumber
for _ in range(int(input())):
    numberOfRounds = int(input())
    
    scoreChef = 0
    scoreMonty = 0

    for _ in range(numberOfRounds):
        chef,monty = map(int,input().split())
        if chef > 9:
            chef = divideStringIntoIndividualIntegersAndSum(chef)
        if monty > 9:
            monty = divideStringIntoIndividualIntegersAndSum(monty)
        
        if chef == monty:
            scoreChef += 1
            scoreMonty += 1
        elif chef > monty:
            scoreChef += 1
        else:
            scoreMonty += 1
    

    if scoreChef == scoreMonty:
        print("2",scoreChef)

    elif scoreChef > scoreMonty:
        print("0",scoreChef)

    else:
        print("1",scoreMonty)