# Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and
# Backtracking for n-queens problem

print("Enter the N*N value for chess board : ",end = " ")
N = int(input())

Queen = "Q"
empty = "-"
# N = 4
# [
# [0, 0, 0, 0,]
# [0, 0, 0, 0,]
# [0, 0, 0, 0,]
# [0, 0, 0, 0,]
# ]

b = [[empty] * N for i in range(N)]


# for j in range(N):
#     temp = []
#     for i in range(N):
#         temp.append(0)
#     b.append(temp)

# print(b)

def isSafe(i, j):
    for p in range(N):
        if b[i][p] == Queen or b[p][j] == Queen:
            return False
    for n in range(N):
        for m in range(N):
            if i + j == n + m or i-j == n-m:
                if b[n][m] == Queen:
                    return False
    return True


def nqueen(noq):
    if noq == 0:
        return True

    for i in range(N):
        for j in range(N):
            if b[i][j] != Queen and isSafe(i,j):
                b[i][j] = Queen
                if nqueen(noq - 1) == True:
                    return True
                b[i][j] = empty
    return False

def printBoard(b):
    for i in b:
        print(i)

if nqueen(N):
    printBoard(b)
else:
    print("Can't Place")

