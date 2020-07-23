def findAns(arrA,arrB):
    if len(arrA) != len(arrB):
        return -1

    da = {}
    db = {}
    arrA.sort()
    arrB.sort()
    
    for a in arrA:
        if a not in da:
            da[a] = 1
        else:
            da[a] += 1
    for b in arrB:
        if b not in db:
            db[b] = 1
        else:
            db[b] += 1
    
    resA = []
    resB = []
    similar = {}

    curr_min = 10**9
    for a in da:
        if a in db and db[a] == da[a]:
            similar[a] = da[a]
            if a <curr_min:
                curr_min = a
        elif a in db :
            curr = max(da[a] , db[a]) - min(da[a] , db[a])

            if da[a] > db[a] and  curr%2 == 0:
                currList = [a] * (curr//2)
                resA.extend(currList)
                if a < curr_min:
                    curr_min = a
            elif curr%2 == 0:
                if a < curr_min:
                    curr_min = a
                
            else:
                # print("1",da[a] , db[a], curr)
                return -1
        elif da[a]%2 == 0:
            curr = da[a]
            currList = [a] * (curr//2)
            resA.extend(currList)
        else:
            # print("2",da[a])
            return -1

    for b in db:
        if b in da and db[b] == da[b]:
            continue
        elif b in da :
            curr = max(da[b] , db[b]) - min(da[b] , db[b])

            if db[b] > da[b] and  curr%2 == 0:
                currList = [b] * (curr//2)
                resB.extend(currList)
                if a < curr_min:
                    curr_min = a
            elif curr%2 == 0:
                if a <curr_min:
                    curr_min = a
                
            else:
                # print("3",db[b] , da[b], curr)
                return -1
        elif db[b]%2 == 0:
            curr = db[b]
            currList = [b] * (curr//2)
            resB.extend(currList)
        else:
            # print("4" , db[b])
            return -1
    
    if len(resA) != len(resB):
        return -1
    resA.sort()
    resB.sort()
    # print(resA)
    # print(resB)
    # print(curr_min)
    i1= 0 
    i2 = len(resA)-1
    j1 = 0
    j2 = len(resB)-1
    ans = 0
    count = 0
    while count != len(resA):
        if resA[i1]< resB[j1]:
            curr = resA[i1]
            if curr <= 2*curr_min:
                ans += curr
                if curr < curr_min:
                    curr_min = curr
            else:
                ans+= 2*curr_min
            i1 += 1
            j2 -= 1
            # resA.pop(0)
            # resB.pop()
                
        else:
            curr = resB[j1]
            if curr <= 2*curr_min:
                ans += curr
                if curr < curr_min:
                    curr_min = curr
            else:
                ans+= 2*curr_min
            
            j1 += 1
            i2 -= 1
        count += 1
    return ans
    


for _ in range(int(input())):
    n = int(input())

    arrA = list(map(int,input().split()))

    arrB = list(map(int,input().split()))

    print(findAns(arrA,arrB))


# for _ in range(1):
#     n = 7

#     arrA = [1,1,3,8,8]

#     arrB = [5,5,3,9,9]

#     print(findAns(arrA,arrB))
