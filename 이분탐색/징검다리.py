# https://programmers.co.kr/learn/courses/30/lessons/43236

distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2

def getDistance(distance, rocks):
    disList = [rocks[0]]
    for i in range(1, len(rocks)):
        disList.append(rocks[i] - rocks[i-1])
    disList.append(distance - rocks[-1])
    return disList

def solution(distance, rocks, n):
    rocks.sort()
    disList = getDistance(distance, rocks)
    print(rocks)
    print(disList)

    answer = 0
    return answer

print(solution(distance, rocks, n))