# https://programmers.co.kr/learn/courses/30/lessons/72413

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

def dsolution(n, s, a, b, fares):
    

def solution(n, s, a, b, fares):
    inf = float("inf")
    matrix = [[inf for j in range(n)] for i in range(n)]
    for i in range(n):
        matrix[i][i] = 0
    
    for fare in fares:
        matrix[fare[1]-1][fare[0]-1] = fare[2]
        matrix[fare[0]-1][fare[1]-1] = fare[2]

    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if (matrix[start][end] > matrix[start][mid] + matrix[mid][end]):
                    matrix[start][end] = matrix[start][mid] + matrix[mid][end]

    answer = inf
    for k in range(n):
        answer = min(answer, matrix[s-1][k] + matrix[k][a-1] + matrix[k][b-1])

    return answer

print(dsolution(n, s, a, b, fares))