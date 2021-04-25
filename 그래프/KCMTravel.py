
import heapq
def saveRouteInfo(routes, routeInfo):
    if (routeInfo[0] in routes):
        route = routes[routeInfo[0]]
        route.append([routeInfo[3], routeInfo[2], routeInfo[0], routeInfo[1]])
        routes[routeInfo[0]] = route
    else:
        routes[routeInfo[0]] = [[routeInfo[3], routeInfo[2], routeInfo[0], routeInfo[1]]]

def dijkstra(routes, N, M):
    # 최단거리를 저장할 배열
    timeTable = [[float('inf') for col in range(N+1)] for row in range(N+1)]

    # fastest[i] = [[해당 노드까지의 시간, 비용]]
    tripInfo = [[float('inf'), 0] for col in range(N+1)]
    tripInfo[1] = [0,0]
 
    readyQ = []
    curNode = 1
    nextRoutes = routes[curNode]
    for nextRoute in nextRoutes:
        heapq.heappush(readyQ, nextRoute)

    while (readyQ):
        curTrip = heapq.heappop(readyQ)
        if (tripInfo[curTrip[3]][1] + curTrip[1] > M): continue
        tripInfo[curTrip[3]][0] += curTrip[0]
        tripInfo[curTrip[3]][1] += curTrip[1]
        nextRoutes = routes[curNode]
        for nextRoute in nextRoutes:
            heapq.heappush(readyQ, nextRoute)

def func(N, M, K):
    # 경로 정보. {현 공항 : [[시간, 비용, 출발지, 목적지]]} 
    routes = {}

    # 정보를 집어 넣음
    for k in range(K):
        routeInfo = list(map(int,sys.stdin.readline().split()))
        saveRouteInfo(routes, routeInfo)
    
    answer = float('inf')
    answer = dijkstra(routes, N, M)
    
    if (answer = float('inf')): return 'Poor KCM'
    else: return answer

sys.stdin = open("KCMTravel.txt","r")
T = int(sys.stdin.readline().rstrip())
for testCase in range(T):
    firstLine = list(map(int,sys.stdin.readline().split()))
    N = firstLine[0]
    M = firstLine[1]
    K = firstLine[2]
    print(func(N, M, K))
