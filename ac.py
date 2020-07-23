import math

def findSubsequence(numbers, k):
    # Write your code here
    numbers.sort()
    currDivisor = numbers[len(numbers)-k-1]
    print(currDivisor)
    while currDivisor!= 1:
        curr = 0
        arr = []
        for x in numbers:
            if x%currDivisor == 0:
                curr += 1
                arr.append(x)
        print("Curr  = ",curr)
        if curr >= k:
            print(currDivisor)
            return arr
        currDivisor -= 1
    print("Not found")
    return numbers[:k]


print(findSubsequence([1,2,8,5,6], 2))

arr = [1,2,3,4]
print(arr[:2])