
def createSegmentTreeLeftRight(arr1, arr2):
    n = len(arr1)
    segmentTree = {}
    for i in range(n):
        segmentTree[i] = [[i]]

    for i in range(len(arr1)-1):
        curr = [arr1[i]]
        curr2 = [i]
        start = arr1[i]
        j = i + 1
        found = False
        while j < n:
            if start <= arr1[j] or found == True:
                segmentTree[i].append(-1)
                found = True
                j += 1
            elif curr[-1] > arr1[j]:
                curr.append(arr1[j])
                curr2.append(j)
                new_list = curr2.copy()

                segmentTree[i].append(new_list)
                j += 1
            else:
                curr.pop()
                curr2.pop()

    return segmentTree


def createSegmentTreeRightLeft(arr1, arr2):
    n = len(arr1)
    segmentTree = {}
    for i in range(n):
        segmentTree[i] = [[i]]

    for i in range(len(arr1)-1, 0, -1):
        curr = [arr1[i]]
        curr2 = [i]
        start = arr1[i]
        j = i - 1
        found = False
        while j > -1:

            if start <= arr1[j] or found == True:
                segmentTree[i].append(-1)
                found = True
                j -= 1
            elif curr[-1] > arr1[j]:
                curr.append(arr1[j])
                curr2.append(j)
                new_list = curr2.copy()

                segmentTree[i].append(new_list)
                j -= 1
            else:
                curr.pop()
                curr2.pop()

    return segmentTree


def findAns1(arr1, arr2, i, j, segmentDict):
    currIndexes = segmentDict[i][j-i]
    if currIndexes == -1:
        return -1
    ans = 0
    for index in currIndexes:
        ans += arr2[index]
    return ans


def findAns2(arr1, arr2, i, j, segmentDict):
    currIndexes = segmentDict[i][i-1]
    if currIndexes == -1:
        return -1
    ans = 0
    # print(i, j,currIndexes)
    for index in currIndexes:
        ans += arr2[index]
    return ans

n,q = map(int,input().split())

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))


segmentTree1 = createSegmentTreeLeftRight(arr1,arr2)
# print(segmentTree1)

segmentTree2 = createSegmentTreeRightLeft(arr1,arr2)
# print(segmentTree2)

for _ in range(q):
    a,b,c = map(int,input().split())


    if a == 1:
        arr2[b-1] = c

    else:
        if b <= c:
            print(findAns1(arr1,arr2,b-1,c-1,segmentTree1))
        else:
            print(findAns2(arr1,arr2,b-1,c-1,segmentTree2))

# n, q = 5, 1

# arr1 = [3,1,4,1,5]
# arr2 = [1, 2, 4, 8, 16]

# segmentTree1 = createSegmentTreeLeftRight(arr1, arr2)
# print(segmentTree1)

# segmentTree2 = createSegmentTreeRightLeft(arr1, arr2)
# print(segmentTree2)


# for _ in range(q):
#     a, b, c = 2, 5, 2

#     if a == 1:
#         arr2[b-1] = c

#     else:
#         if b <= c:
#             print(findAns1(arr1, arr2, b-1, c-1, segmentTree1))
#         else:
#             print(findAns2(arr1, arr2, b-1, c-1, segmentTree2))
