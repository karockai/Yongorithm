# https://programmers.co.kr/learn/courses/30/lessons/49191

n = 5
results =  [[4,3],[4,2],[3,2],[1,2],[2,5]]


def getGraph(results):
    # graph = {선수번호 : [이긴 번호]}
    graphList = []
    winGraph = {}
    loseGraph = {}
    
    for result in results:
        # getWin
        if (result[0] in winGraph):
            winGraph[result[0]].append(result[1])
        else:
            winGraph[result[0]] = [result[1]]

        # getLose
        if (result[1] in loseGraph):
            loseGraph[result[1]].append(result[0])
        else:
            loseGraph[result[1]] = [result[0]]

    graphList.append(winGraph)
    graphList.append(loseGraph)

    return graphList

def DFS(graph, curNode, visited, metNum):
    visited[curNode] = True
    metNum += 1
    
    if (curNode in graph):
        for nextNode in graph[curNode]:
            if (nextNode in visited): continue
            metNum = DFS(graph, nextNode, visited, metNum)
    
    return metNum
    

def getCnt(graphList, n):
    answer = 0
    visited = {}

    for startNode in range(1, n+1):
        result = 1
        visited.clear()
        if (startNode in graphList[0]):
            for nextNode in graphList[0][startNode]:
                if (nextNode in visited): continue
                result += DFS(graphList[0], nextNode, visited, 0)

        if (startNode in graphList[1]):
            for nextNode in graphList[1][startNode]:
                if (nextNode in visited): continue
                result += DFS(graphList[1], nextNode, visited, 0)
        # print('start : {0}, result : {1}'.format(startNode, result))
        # print(visited)
        if (result == n):answer += 1

    return answer

def solution(n, results):
    graphList = getGraph(results)
    answer = getCnt(graphList, n)
    return answer

print(solution(n, results))