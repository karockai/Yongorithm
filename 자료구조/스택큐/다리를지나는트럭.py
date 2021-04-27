# https://programmers.co.kr/learn/courses/30/lessons/42583
# bridge_length = 2 
# weight = 10
# truck_weights = [7,4,5,6]


bridge_length = 100 
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


def solution(bridge_length, weight, truck_weights):
    from collections import deque

    readyQ = deque(truck_weights)
    bridge = deque()
    bridgeWeight = 0
    time = 0
    
    
    while (readyQ or bridge):
        time += 1

        while (bridge and bridge[0][1] <= time):
            exitTruck = bridge.popleft()
            bridgeWeight -= exitTruck[0] 

        if (readyQ and weight >= bridgeWeight + readyQ[0]):
            curTruck = readyQ.popleft()
            # 언제 빼낼것인지도 기록
            bridge.append([curTruck, time + bridge_length])
            bridgeWeight += curTruck

    return time

print(solution(bridge_length, weight, truck_weights))