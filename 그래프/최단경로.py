# https://www.acmicpc.net/problem/1753

import heapq
import sys
def inputRoutes(source, dest, point, routes):
    # routes = {source : (point, prev, dest)}
    if (not source in routes):
        routes[source] = []
    routes[source].append((point, source, dest))

def dijkstra(start, routes, V):
    # fastPath 는 start로부터 node까지의 최단 비용과 경로를 저장한다.
    fastPath = [float('inf') for col in range(V+1)]
    fastPath[start] = 0

    visited = [False for col in range(V+1)]
    visited[start] = True

    # readyQ[0] =  start로부터 가장 가까운 미방문 Node가 들어있다.
    readyQ = []
    # nextRoute = (point, prev, dest)
    nextRoutes = routes[start]
    for nextRoute in nextRoutes:
        if (fastPath[nextRoute[2]] < nextRoute[0]): continue
        heapq.heappush(readyQ, (nextRoute[0], nextRoute))
    
    while (readyQ):
        tmp = heapq.heappop(readyQ)
        cost = tmp[0]
        curRoute = tmp[1]
        if (fastPath[curRoute[2]] < fastPath[curRoute[1]] + curRoute[0]): continue

        fastPath[curRoute[2]] = cost

        if (curRoute[2] in routes and visited[curRoute[2]] == False):
            newRoutes = routes[curRoute[2]]
            for newRoute in newRoutes:
                
                if (fastPath[newRoute[2]] < fastPath[curRoute[2]] + newRoute[0]): continue
                heapq.heappush(readyQ, (fastPath[curRoute[2]] + newRoute[0], newRoute))
            visited[curRoute[2]] = True

    for i in range(1, V+1):
        if (fastPath[i] == float('inf')): print('INF')
        else: print(fastPath[i])

# sys.stdin = open("최단경로.txt","r")

V, E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline().rstrip())
routes = {}

for e in range(E):
    edge = list(map(int,sys.stdin.readline().split()))
    inputRoutes(edge[0], edge[1], edge[2], routes)

dijkstra(K, routes, V)