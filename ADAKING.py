tesCases = int(input())
for tesCase in range(tesCases):
    k = int(input())
    matrix = [[None for i in range(8)] for j in range(8)]

    
    row = k // 8
    col = k - 8*row


    for i in range(row+1):
        for j in range(col):
            matrix[i][j] = "."

    
    for i in range(col,8):
        try:
            matrix[row][i] = "X"
        except:
            pass
    # matrix[row][col] = "X"
    if col%8 != 0 and row < 7:
        for i in range(col+1):
            matrix[row+1][i] = "X"

    
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == None:
                matrix[i][j] = "."


    matrix[0][0] = "O"


    for row in matrix:
        for x in row:
            print(x,end = "")
        print()
