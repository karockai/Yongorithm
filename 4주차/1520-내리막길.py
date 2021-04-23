import sys
sys.stdin = open("input.txt","r")

M, N = map(int,sys.stdin.readline().split())

amap = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
visited = [[-1 for col in range(N)] for row in range(M)]
visited[M-1][N-1] = 1

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def DFS(x,y):
    cnt = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < M and 0 <= ny < N and amap[nx][ny] < amap[x][y]:
            if visited[nx][ny] == -1:
                DFS(nx,ny)
            visited[x][y] += visited[nx][ny]
    visited[x][y] += 1
DFS(0,0)
print(visited[0][0])

