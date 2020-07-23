for _ in range(int(input())):
    n = int(input())

    dx = {}
    dy = {}
    for _ in range(4*n-1):
        x,y = map(int,input().split())

        if x not in dx:
            dx[x] = 1
        else:
            del dx[x]
        if y not in dy:
            dy[y] = 1
        else:
            del dy[y]

    for vertex in dx:
        if dx[vertex] == 1:
            ansx = vertex

    for vertex in dy:
        if dy[vertex] == 1:
            ansy = vertex
    print(ansx,ansy)
    