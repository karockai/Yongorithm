import sys
from math import sqrt
sys.stdin = open("input.txt","r")

# 무엇을 기록?
N = int(sys.stdin.readline().rstrip())
num = [0,1,2,3,4]
chk = [0,1,2,3,1]


def numfinder(i):
    left = 1
    right = i-1
    temp = sys.maxsize
    while left < right:
        temp = min(temp, chk[left]+chk[right])
        left += 1
        right -= 1
    return temp

for i in range(5,N+1):
    num.append(i)
    if sqrt(i) == int(sqrt(i)):
        chk.append(1)
    else:
        chk.append(numfinder(i))

print(chk[N])


    
    
