# 본 문제는 테스트 케이스가 100개까지 이므로 3중 for문을 돌리는 플로이드 - 와샬을 쓸 수 없음
# 본 문제는 아직 방문 안한 노드들을 모두 무한대로 초기 설정해놓는 다익스트라도 쓰기 힘들다. 총 노드가 nm개이기 때문이다. 그러면 10000이 되는 것도 순식간임
from sys import stdin as s
from collections import deque
s = open('./input.txt', 'rt')
n, m = list(map(int, s.readline().strip().split()))
myMap = [list(map(int, s.readline().strip())) for _ in range(n)]
distanceList = [[-1] * m for _ in range(n)]
distanceList[0][0] = 1

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
# 통해서 온 부모의 정보를 기억해야 한다. 통해서 온 부모보다 한칸 더 나아가야 함

queue = deque()
queue.append([0, 0])

while queue:
  tmpY, tmpX = queue.popleft()

  for i in range(4):
    eY = tmpY + dy[i]
    eX = tmpX + dx[i]
    if not (0 <= eY < n and 0 <= eX < m):
      continue

    if myMap[eY][eX] == 1 and distanceList[eY][eX] == -1:
        distanceList[eY][eX] = distanceList[tmpY][tmpX] + 1
        queue.append([eY, eX])

print(distanceList[n -1][m -1])

# 미해결 코드