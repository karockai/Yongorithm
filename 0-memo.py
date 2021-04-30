import sys
import heapq
from collections import deque 
import itertools

sys.stdin = open("input.txt","r")


a = int(sys.stdin.readline().rstrip())


a, b = map(int,sys.stdin.readline().split())

[int(sys.stdin.readline().rstrip()) for _ in range(N)]
a_list = list(map(int,sys.stdin.readline().split()))
a_list = [list(map(int,sys.stdin.readline().split())) for _ in range( )]
matrix = [[0 for col in range(10)] for row in range(10)]

# 전부 분할하기
a = list(a)

# 정수로 받은 숫자를 분리해서 정수로 리스트
number = list(map(int, list(str(sys.stdin.readline()))))


2x2list = [list(map(int,sys.stdin.readline().split())) for _ in range(t)]

#2차원 배열 복사
a = [item[:] for item in list_a]

read = sys.stdin.readline

# 무한
float("inf")


arr = list(range(10))
print(*arr)
N, *array = arr
print(array)


# x[0] -> x[1]순으로 오름차순 정렬
star.sort(key=lambda x: (x[0], x[1]))

# 재귀 깊이
import sys
sys.setrecursionlimit(10**6)

# 붙어있는 숫자들 뗴어네서 리스트화
maze = [list(map(int, list(str(sys.stdin.readline().rstrip())))) for _ in range(N)]


dx = [0,-1,0,1]
dy = [-1,0,1,0]

for d in range(4):
    nx = x + dx[d]
    ny = y + dy[d]


# 정사각형 2차원 배열 회전
def rotate(arr) : # return array 회전한 배열의 결과
    M = len(arr)
    tmpArr = [[0 for _ in range(M)] for _ in range(M)];
    for i in range(M) :
        for j in range(M) :
            tmpArr[j][M-i-1] = arr[i][j];
    return tmpArr

# 리스트를 하나의 문자열로 합치기
l = ['d', 'a', 't', 'a']
print(''.join(l)) #data
print('_'.join(l)) #d_a_t_a
