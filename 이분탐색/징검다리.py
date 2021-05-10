# https://programmers.co.kr/learn/courses/30/lessons/43236

distance = 34
rocks =  [5, 19, 28]
n = 2

def solution(distance, rocks, n):

    rocks.sort()
    rocks.append(distance)
    # print('rocks:', rocks)
    low = 0
    high = distance
    mid = (low + high) // 2

    while (low <= mid):
        
        # print('low:', low, 'mid:', mid, 'high:', high)
        prev = 0
        rmCnt = 0

        for i in range(len(rocks)):
            dis = rocks[i] - prev
            # print('cur:', rocks[i], 'prev:', prev)
            if (dis < mid):
                rmCnt += 1
            else:
                prev = rocks[i]
        
        # print('prev', prev)

        # print('rn:', rmCnt)
        # if (rmCnt == n):
        #     return mid
        if (rmCnt <= n):
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    return mid

print(solution(distance, rocks, n))