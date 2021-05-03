# https://programmers.co.kr/learn/courses/30/lessons/42839

numbers = '011'

def getPrimeList(maxNum):
    import math

    n = maxNum # 2부터 1,000까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화

    # 에라토스테네스의 체 알고리즘 
    for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2 
            while i * j <= n:
                array[i * j] = False
                j += 1
    array[1] = False
    array[0] = False
    return array


def solution(numbers):
    numList = list(numbers)
    numList.sort(reverse=True)
    maxNum = numList[0]
    for i in range(1,len(numList)):
        maxNum += numList[i]
    primeList = getPrimeList(int(maxNum))
    
    # numList = list(map(int, list(str(numbers))))
    import itertools
    visited = {}
    answer = 0
    for j in range(1, len(numList)+1):
        arrays = list(itertools.permutations(numList, j))

        for array in arrays:
            aList = list(array)
            curNum = aList[0]
            for i in range(1, len(aList)):
                curNum += aList[i]
            
            curNum = int(curNum)
            if (curNum in visited): continue
            if (not primeList[curNum]): continue
            # print(curNum)
            answer += 1
            visited[curNum] = True

    return answer


print(solution(numbers))