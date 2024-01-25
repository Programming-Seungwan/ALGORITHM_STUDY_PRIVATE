from sys import stdin as s
# 이 문제는 python3로는 안되고 인터프리터 설정을 pypy로 하면 됨
#s = open('./input.txt', 'rt')

N = int(s.readline().strip())
# 어떻게 퀸끼리 서로 공격할 수 없는 위치인가를 판단하는 것이 중요한 문제. 퀸은 사방향, 대각선 모두 공격이 가능하다

# 각 행에는 퀸이 하나씩 위치하는데, 다음 행에 퀸을 위치시킬 때마다 promising 한 지를 검사한다
ans = 0
row = [0] * N

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == N:
        ans += 1
        return

    else:
        for i in range(N):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)