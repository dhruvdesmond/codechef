for _ in range(int(input())):
    numberPluck = int(input())
    arr = list(map(int,input().split()))
    ans  = 0

    # iterate over arr given from first index to second last
    # and compare distance between two strings and minus 1
    # keep adding the res to ans
    for index in range(len(arr)-1):
        c1 = arr[index]
        c2 = arr[index+1]

        ans += max(c1,c2)-min(c1,c2)-1
    print(ans)