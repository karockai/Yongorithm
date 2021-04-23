# https://programmers.co.kr/learn/courses/30/lessons/42898

m = 4 
n = 3 
puddles = [[2, 2]]

def setPuddle(puddles, aMap):
    for puddle in puddles:
        aMap[puddle[1]-1][puddle[0]-1] = -1
    return aMap

def row1(aMap):
    row = aMap[0]
    puddle = False
    for r in range(1,len(row)):
        if (puddle):
            row[r] = 0
            continue
        if (row[r] == -1):
            row[r] = 0
            puddle = True
        else:
            row[r] = 1
    return aMap

def col1(aMap):
    puddle = False
    for r in range(1,len(aMap)):
        if (puddle):
            aMap[r][0] = 0
            continue
        if (aMap[r][0] == -1):
            aMap[r][0] = 0
            puddle = True
        else:
            aMap[r][0] = 1
    return aMap

def solution(m, n, puddles):
    aMap = [[0 for col in range(m)] for row in range(n)]
    aMap = setPuddle(puddles, aMap)
    aMap = row1(aMap)
    aMap = col1(aMap)

    for i in range(1,n):
        for j in range(1,m):
            if (aMap[i][j] == -1):
                aMap[i][j] = 0
            else:
                aMap[i][j] = aMap[i-1][j] + aMap[i][j-1]
                
    return aMap[n-1][m-1]%1000000007

print(solution(m,n,puddles))