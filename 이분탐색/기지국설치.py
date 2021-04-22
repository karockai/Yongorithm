# https://programmers.co.kr/learn/courses/30/lessons/12979

n = 11
stations = [4, 11]
w = 1

n = 16
stations = [9]
w= 2

def getInstallNum(length, armRange):
    if (length % (armRange*2+1)):
        num = length // (armRange*2+1) + 1
    else:
        num = length // (armRange*2+1)
    return num

def solution(n, stations, w):
    answer = 0
    armRange = w

    apt = n+1

    while (0 < apt):
        # 중계기 범위 안에 있는 경우
        apt -= 1
        if (stations):
            lastStation = stations.pop()
            if (apt <= lastStation + w):
                apt = lastStation - w
            else:
                not5G = apt - (lastStation + armRange)
                answer += getInstallNum(not5G, armRange)
                apt = lastStation - armRange
        else:
            answer += getInstallNum(apt, armRange)
            apt = -1

    return answer

print(solution(n, stations, w))