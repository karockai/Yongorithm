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



def solution(n, computers):
    answer = 0
    isolation = False
    for i in range(n):
        curNetwork = deque()
        notIsolation = False
        for j in range(n):
            if not computers[i][j]:continue
            # 현 컴에 연결된 컴 추가
            curNetwork.append([i,j])
            computers[i][j] = 0
            computers[j][i] = 0
            notIsolation = True

        while (True):
            for l in range(len(curNetwork)):
                nextCom = curNetwork.popleft()
                for k in range(n):
                    if not computers[nextCom[1]][k]:continue
                    curNetwork.append([nextCom[1],k])
                    computers[nextCom[1]][k] = 0
                    computers[k][nextCom[1]] = 0
            if not curNetwork:
                break
        
        if (notIsolation):
            answer += 1
    
    return answer

print(solution(n, computers))