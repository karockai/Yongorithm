# https://www.acmicpc.net/problem/1963
import sys
import copy
from collections import deque 

primeList = {}

    
def getPrimeList():
    global primeList
    import math
    
    n = 9999 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화

    # 에라토스테네스의 체 알고리즘 
    for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2 
            while i * j <= n:
                array[i * j] = False
                j += 1

    # 모든 소수 출력
    for i in range(1000, n + 1):
        if array[i]:
            primeList[i] = True

def isInList(num):
    global primeList
    if (num in primeList):
        return True
    return False

def isVisited(num):
    global visited
    if (num in visited): return True
    else:
        visited[num] = True
        return False

def parsing(num):
    parsingList = []
    parsingList.append(num//1000)
    parsingList.append((num//100)%10)
    parsingList.append((num//10)%10)
    parsingList.append(num%10)
    return parsingList

def listToNum(a_list):
    num = 0
    for i in range(len(a_list)):
        num += a_list[i] * 10**(3-i)
    return num

def BFSMain():
    global primeList
    global bfrPrime, aftPrime, bfrList, aftList
    lv = 0
    
    que = deque()
    que.append(bfrPrime)
    find = False

    while (True):
        for queIdx in range(len(que)):
            curNum = que.popleft()
            if (curNum == aftPrime):
                find = True
                break

            if (find): break
            
            parsingList = parsing(curNum)
            
            for i in range(len(parsingList)):
                for j in range(0,10):
                    if (i == 0 and j == 0): continue
                    newNumList = copy.deepcopy(parsingList)
                    newNumList[i] = j
                    newNum = listToNum(newNumList)
                    
                    if not (isInList(newNum)): continue
                    if (isVisited(newNum)): continue
                    que.append(newNum)
        if (find or len(que) == 0): break
        lv += 1
    
    if (find):return lv
    else: return -1


getPrimeList()
sys.stdin = open("소수경로.txt","r")
N = int(sys.stdin.readline().rstrip())
for cnt in range(N):
    visited = {}
    bfrPrime = None
    aftPrime = None
    startList = list(map(int,sys.stdin.readline().split()))
    bfrPrime = startList[0]
    aftPrime = startList[1]
    result = BFSMain()
    if (result == -1): print('Impossible')
    else: print(result)

    
    



    