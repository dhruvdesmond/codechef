def countSubarray(arr,x,y,l,r):
    count = 0
    for i in range(x,y+1):
        curr = arr[i]
        for j in range(i,y+1):
            curr = max(curr,arr[j])
            if curr >= l and curr <= r:
                count += 1
            else:
                continue
    return count


n,q,l,r = map(int,input().split())
arr = [0]*n
for _ in range(q):
    query,x,y = map(str,input().split())

    if query == "1":
        arr[int(x)-1] = int(y)
    else:
        print(countSubarray(arr,int(x)-1,int(y)-1,l,r))
     