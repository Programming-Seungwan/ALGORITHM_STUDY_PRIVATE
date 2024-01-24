# N과 M이 주어짐
from sys import stdin as s

#s = open('./input.txt', 'rt')

N, M = list(map(int, s.readline().strip().split()))

num = [i for i in range(1, N + 1)]
res = []

def recur(start):
  if len(res) == M:
    print(' '.join(map(str, res)))
    return

  for j in range(start, N):
    res.append(num[j])
    recur(j + 1)
    res.pop()

recur(0)