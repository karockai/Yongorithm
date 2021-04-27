
n=3
k=5



# [n-1명, n-2명, n-3명, ... , 1명]
import math

1. n-1명에서 순열의 갯수를 구한다.
2. n-1 // 갯수 + 1 이 첫 요소가 된다.
3. n-2명에서 반복 (재귀)
4. 

def recur(left, ans):

def solution(n, k):
    lane = []
    for i in range(n):
        lane.append(i+1)
