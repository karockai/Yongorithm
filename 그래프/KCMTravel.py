

def func(N, M, K):





sys.stdin = open("KCMTravel.txt","r")
T = int(sys.stdin.readline().rstrip())
for testCase in range(T):
    firstLine = list(map(int,sys.stdin.readline().split()))
    N = firstLine[0]
    M = firstLine[1]
    K = firstLine[2]
    print(func(N, M, K))
