# 최소 히프가 아니라 최대 히프로 구현해야하는 문제일 수도 있다
from sys import stdin as s
import heapq # 해당 자료형은 배열 자체가 정렬되어 있는 것은 아니다. 이걸 트리 구조로 만들었을 때 느슨한 정렬이 되어 있는 것이다
s = open('./input.txt', 'rt')
n = int(s.readline())

minHeapArray = []

for _ in range(n):
  # 숫자를 받아들여서 넣어준다.
  tmpArr = [int(item) for item in s.readline().split(' ')]
  for i in range(n):
    heapq.heappush(minHeapArray, (-tmpArr[i], tmpArr[i]))

for i in range(n):
  if (i == (n - 1)):
    print(heapq.heappop(minHeapArray)[1])
  else:
    heapq.heappop(minHeapArray)