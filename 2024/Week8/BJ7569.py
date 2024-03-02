import sys
from collections import deque

m, n, h = map(int, input().split())

matrix = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

queue = deque()

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

answer = 0

def bfs(): # 해당 함수 내에서 큐에 넣어놓고 시작하지 않고, 초기 조건에서 이미 익은 것들을 넣고 시작한다. 다시 방문할 필요가 없으므로
    while queue:
        x,y,z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue

            if matrix[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                queue.append((nx,ny,nz))
                matrix[nx][ny][nz] = matrix[x][y][z] + 1 # 인접한 것들 다음 스텝에서 익는 것이 진행되기 때문이다
                visited[nx][ny][nz] = True


# 모두 1이 아닐 경우

for a in range(h):
    for b in range(n):
        for c in range(m):
            if matrix[a][b][c] == 1 and visited[a][b][c] == 0:
                queue.append((a,b,c))
                visited[a][b][c] = True
bfs()

# 토마토 확인

for a in matrix:
    for b in a:
        for c in b:
            if c == 0:
                print(-1) # 아직 바뀌지 않은 것이 있다면 -1을 출력하고 종료
                exit(0)
        answer = max(answer, max(b))

print(answer-1)

# 어차피 모두 1이라면 0이 출력된다.