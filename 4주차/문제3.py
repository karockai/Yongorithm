import sys
sys.stdin = open("input.txt","r")

# 한 가방에는 한 보석만 들어간다.
#  -> 가장 높은 가치의 보석을 가장 용량이 작은 가방에 넣어야됨

N, K = map(int,sys.stdin.readline().split())
jewelry = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
bag = [int(sys.stdin.readline().rstrip()) for _ in range(K)]
bag_chk = [0]*K

jewelry.sort(key=lambda x: (x[1], x[0]), reverse=True)
bag.sort()
value = 0
for j in range(len(jewelry)):
    if sum(bag_chk) == len(bag):
        break
    for b in range(len(bag)):
        if jewelry[j][0] <= bag[b] and bag_chk[b] == 0:
            value += jewelry[j][1]
            bag_chk[b] = 1
            break


print(value)
             



