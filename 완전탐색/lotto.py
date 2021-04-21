# https://www.acmicpc.net/problem/6603

k = None
S = None

def input():
    global k
    global S
    
    inputText = open("lotto.txt","r")
    lineList = inputText.read().splitlines()
    print(lineList)
    for i in lineList:
        print(i)
    
    ex = [1, 2, 3]
    for j in ex:
        print(j)
    

input()
