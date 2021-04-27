# https://programmers.co.kr/learn/courses/30/lessons/12914


n = 4
n = 5

# 1, 2, 3, 5

def solution(n):
    if (n == 1):
        return 1
    elif (n == 2):
        return 2
    aMap = [0 for col in range(n)]

    aMap[0] = 1
    aMap[1] = 2
    for i in range(2, n):
        aMap[i] = aMap[i-1] + aMap[i-2]
    
    return = aMap[-1] % 1234567