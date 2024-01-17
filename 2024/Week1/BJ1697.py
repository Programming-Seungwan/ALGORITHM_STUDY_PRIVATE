# from sys import stdin as s
# from collections import deque

# s = open('./input.txt', 'rt')

# startPoint, goalPoint = list(map(int, s.readline().strip().split(' ')))

# memoArray = [0 for _ in range(100001)]
# checkArray = [False for _ in range(100001)]

# def bfs(sPoint, gPoint):
#   queue = deque()
#   queue.append(sPoint)

#   checkArray[sPoint] = True
#   # 큐에서 뽑아서 근처에 있는 것들을 탐색함
#   while queue:
#     tmpPoint = queue.pop()
#     if tmpPoint == gPoint:
#       print(memoArray[tmpPoint] )
#       break
#     for nPoint in (tmpPoint - 1, tmpPoint + 1, tmpPoint * 2):
#       if 0 <= nPoint <= 100000 and checkArray[nPoint] == False:
#         memoArray[nPoint] = memoArray[tmpPoint] + 1
#         checkArray[nPoint] = True
#         queue.append(nPoint)

# bfs(startPoint, goalPoint)

import sys
from collections import deque

def bfs(v):
    q = deque([v]) #큐 구현을 위해 deque 사용
    while q:
        v = q.popleft()
        if v == k:
            return visited[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)

n, k = map(int, sys.stdin.readline().split())
visited = [0 for i in range(100001)]
print(bfs(n))