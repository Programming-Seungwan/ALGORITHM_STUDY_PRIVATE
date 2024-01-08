import sys

input = sys.stdin.readline



n,m = map(int, input().split())
totalMap = [list(map(int, input().split())) for _ in range(n)]
checkMap = [[False] * m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

# bfs 함수는 특정 지점부터 시작하여 너비 우선 탐색을 진행함
def bfs(y, x):
    # 해당함수는 bfs를 실행하여 얻은 그림의 넓이를 반환함
    result = 1
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        for u in range(4):
            ny = ey + dy[u]
            nx = ex + dx[u]
            if 0 <= ny < n and 0 <= nx < m:
                if totalMap[ny][nx] == 1 and checkMap[ny][nx] == False:
                    result += 1
                    checkMap[ny][nx] = True
                    q.append((ny, nx))

    return result

count = 0
maxValue = 0
for j in range(n):
    for i in range(m):
        if totalMap[j][i] == 1 and checkMap[j][i] == False:
            checkMap[j][i] = True
            count += 1
            maxValue = max(maxValue, bfs(j, i))

print(count)
print(maxValue)