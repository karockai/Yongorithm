# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3
from collections import deque 

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]


# 110
# 110
# 001

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
# 110
# 111
# 011    

def delNetwork(computers, que, x,y):
    que.append(y)
    computers[x][y] = 0
    computers[y][x] = 0
    return que

def solution(n, computers):
    answer = 0
    isolation = False
    for i in range(n):
        curNetwork = deque()
        notIsolation = False
        for j in range(n):
            if not computers[i][j]:continue
            curNetwork = delNetwork(computers, curNetwork, i, j)
            notIsolation = True

        while (True):
            for length in range(len(curNetwork)):
                nextCom = curNetwork.popleft()
                for k in range(n):
                    if not computers[nextCom][k]:continue
                    curNetwork = delNetwork(computers, curNetwork, nextCom, k)

            if not curNetwork:
                break
        
        if (notIsolation):
            answer += 1
    
    return answer

print(solution(n, computers))