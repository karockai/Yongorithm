v = [20,8,1,10,4,15]

def getEndValue(v):
    length = len(v)
    mid = length//2
    v.sort()
    
    lenIsEven = None
    lenIsEven = True if (not length % 2) else False
    
    if (lenIsEven):
        start = v[mid -1]
        end = v[mid]
    else:
        start = v[mid]
        end = v[mid-1] if (abs(v[mid] - v[mid-1]) < abs(v[mid] - v[mid+1])) else v[mid+1]

    v.remove(start)
    v.remove(end)

    return (start, end)

def cal(aList):
    value = 0

    for i in range(len(aList)-1):
        value += abs(aList[i] - aList[i+1])

    return value

def solution(v):
    if (len(v) == 2):return abs(v[0]-v[1])

    tmp = getEndValue(v)
    start, end = tmp[0], tmp[1]

    import itertools
    arrays = list(itertools.permutations(v, len(v)))
    answer = 0

    for array in arrays:
        aList = [start]

        for num in array:
            aList.append(num)

        aList.append(end)
        answer = max(answer, cal(aList))
    
    return answer

print(solution(v))