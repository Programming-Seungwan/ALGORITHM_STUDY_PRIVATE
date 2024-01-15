# DFS
import sys
sys.setrecursionlimit(10**6) # 재귀의 깊이 변경 (RecursionError)

from sys import stdin as s

# s= open('./input.txt', 'rt')


m, n, k = map(int, s.readline().strip().split())
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, s.readline().strip().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

def dfs(x, y):
    global count
    # 범위에서 나갔거나 이미 방문한 경우에 dfs는 돌지 않음
    if x<0 or x>=m or y<0 or y>=n:
        return 0
    if graph[x][y] == 1:
        return 0

    graph[x][y] = 1
    count += 1
    for i in range(4):
        dfs(x+dx[i], y+dy[i])

    return count

result = []

for i in range(m):
    for j in range(n):
        cnt = dfs(i,j)
        if cnt:
            result.append(cnt)
            count = 0

result.sort()
print(len(result))
for i in result:
    print(i, end=' ')