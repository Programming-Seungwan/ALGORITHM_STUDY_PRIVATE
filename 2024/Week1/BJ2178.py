# 해당 문제는 일단 미해결 상태로 커밋

from sys import stdin as s
from collections import  deque

# s=open("./input.txt","rt")

[n,m] = map(int, s.readline().strip().split(" "))

totalMap = []
for _ in range(n):
    totalMap.append(list(map(int, s.readline().strip())))

checkMap = [[False] * m for _ in range(n)]


dy = [0, 1, 0, -1]
dx = [1, 0 ,-1, 0]

def bfs(y, x):
    checkMap[0][0] = 1
    queue = deque()
    queue.append((y,x))

    while queue:
        ey, ex = queue.pop()
        for u in range(4):
            ny = ey + dy[u]
            nx = ex + dx[u]
            if 0 <= ny < n and 0 <= nx < m:
                if totalMap[ny][nx] == 1 and checkMap[ny][nx] == False:
                    checkMap[ny][nx] = checkMap[ey][ex] + 1
                    queue.append((ny, nx))



    return checkMap[n-1][m-1]

print(bfs(0,0))