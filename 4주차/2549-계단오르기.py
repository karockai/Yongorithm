import sys
sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline().rstrip())
stair = [0]
[stair.append(int(sys.stdin.readline().rstrip()) )for _ in range(N)]

if N == 1:
    print(stair[1])
    quit()
elif N == 2:
    print(stair[1]+stair[2])
    quit()

point = [0] * (N+1)
point[1] = stair[1]
point[2] = (stair[1]+stair[2])

for n in range(3,N+1):
    point[n] = max(point[n-3]+stair[n-1], point[n-2]) + stair[n]


print(point[N])
    


