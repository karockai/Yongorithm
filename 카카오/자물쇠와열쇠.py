# https://programmers.co.kr/learn/courses/30/lessons/60059


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# 000
# 100
# 011

lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# 111
# 110
# 101

# 모든 lock의 홈에 대해서, key의 돌기부분을 하나씩 맞추고, 90도씩 돌려가면서 해본다.

# m : 행렬, d : 회전 방향, 90도*d
def rotate(arr) : # return array 회전한 배열의 결과
    M = len(arr)
    tmpArr = [[0 for _ in range(M)] for _ in range(M)];
    for i in range(M) :
        for j in range(M) :
            tmpArr[j][M-i-1] = arr[i][j];
    return tmpArr


from collections import deque 
# import copy

def getLockGroove(lockGroove, lockRamus, lock):
    for i in range(len(lock)):
        for j in range(len(lock[i])):
            if (lock[i][j]):
                lockRamus.append([i,j])
            else:
                lockGroove.append([i,j])

def getKeyRamus(key):
    keyRamus = deque()
    for i in range(len(key)):
        for j in range(len(key[i])):
            if (key[i][j]):
                keyRamus.append([i,j])
    return keyRamus

# grv 한칸에 대해서 key를 맞춰본다.
def judge(keyRamus, lockGroove, lockRamus, lockGSet, lockRSet):
    keyR = [item[:] for item in keyRamus]
    keyStart = keyR[0]
    lockStart = lockGroove[0]
    dx = lockStart[0] - keyStart[0]
    dy = lockStart[1] - keyStart[1]
    
    for i in range(len(keyR)):
        keyR[i][0] += dx
        keyR[i][1] += dy


    keySet = set(list(map(tuple, keyR)))


    if (keySet & lockGSet == lockGSet):
        if (keySet & lockRSet):
            return False
        return True
    return False
    
# key를 하나식 대입해보면서 judge실행
def trySolve(keyRamus, lockGroove, lockRamus, lockGSet, lockRSet):
    for grvLen in range(len(lockGroove)):
        for qLen in range(len(keyRamus)):
            if (judge(keyRamus, lockGroove, lockRamus, lockGSet, lockRSet)):
                return True
            keyRamus.append(keyRamus.popleft())
        lockGroove.append(lockGroove.popleft())
    return False

# 열쇠를 돌려보면서 trySolve 실행
def rotateKey(key, lockGroove, lockRamus, lockGSet, lockRSet):
    for deg in range(4):
        if (deg > 0):
            key = rotate(key)
        keyRamus = getKeyRamus(key)
        if not keyRamus:
            return False

        if (trySolve(keyRamus, lockGroove, lockRamus, lockGSet, lockRSet)):
            return True
    return False

def solution(key, lock):
    lockGroove = deque()
    lockRamus = deque()
    getLockGroove(lockGroove, lockRamus, lock)
    lockGSet = set(list(map(tuple, lockGroove)))
    lockRSet = set(list(map(tuple, lockRamus)))
    if not (lockGroove): return True

    return rotateKey(key, lockGroove, lockRamus, lockGSet, lockRSet)

print(solution(key, lock))