# https://www.acmicpc.net/problem/9935


import sys
sys.stdin = open("문자열폭발.txt","r")

def check(stack, newBomb):
    stackPtr = len(stack) - 1
    for i in range(len(newBomb)-1, -1, -1):
        if (stackPtr < 0): return False
        if (stack[stackPtr] == newBomb[i]): stackPtr -= 1
        else: return False
    return True


def delete(stack, newBomb):
    if (not stack): return
    if (len(stack) < len(newBomb)): return
    if (check(stack, newBomb)):

        for i in range(len(newBomb)):
            stack.pop()
        delete(stack, newBomb)
    return


letters = list(map(str, list(str(sys.stdin.readline().rstrip()))))
bomb = list(map(str, list(str(sys.stdin.readline().rstrip()))))
stack = []

for letter in letters:
    stack.append(letter)
    if (letter == bomb[-1] and len(stack) >= len(bomb)):
        delete(stack, bomb)
        

if (stack):
    print(''.join(stack))
else:
    print('FRULA')



    