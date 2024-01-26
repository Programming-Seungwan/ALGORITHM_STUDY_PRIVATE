# BFS를 활용하여 풀 수도 있음
from itertools import combinations
from collections import deque
import sys
graph = []
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
positions = [(i, j) for i in range(5) for j in range(5)] # 그래프 내의 좌표를 나타낼 자료구조
# 콤비네이션은 가능한 조합들을 iterable한 것으로 반환함
combs = list(combinations(positions, 7))
answer = 0

for _ in range(5):
    graph.append(list(sys.stdin.readline().strip()))


# 주어진 콤비네이션에서 좌표를 뽑아 자도에 해당하는 요소를 검사해 다솜의 개수가 4개 이상인지를 검사하는 함수
def checkDaSom(givenComb):
    daSom = 0
    for x, y in givenComb:
        if graph[x][y] == 'S':
            daSom += 1
    return True if daSom >= 4 else False


# 주어진 좌표 콤비네이션을 활용하여 해당 7개가 모두 이어져있는지를 확인하는 함수
def checkAdjacent(givenComb):
    visit = [False]*7
    q = deque()
    q.append(givenComb[0])
    visit[0] = True # 한 좌표를 방문처리함

    while q:
        x, y = q.popleft()
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            if (nx, ny) in givenComb:
                nextIdx = givenComb.index((nx, ny)) #주어진 콤비네이션에서 몇번쨰인지
                if not visit[nextIdx]:
                    q.append((nx, ny))
                    visit[nextIdx] = True

    return False if False in visit else True # 주어진 콤비네이션이 인접한 것으로, 모두 옆 방문을 할 수 있으면 True를 반환


for comb in combs:
    if checkDaSom(comb):
        if checkAdjacent(comb):
            answer += 1

print(answer)