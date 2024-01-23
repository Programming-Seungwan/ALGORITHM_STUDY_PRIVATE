from sys import stdin
input = stdin.readline

N, S = map(int, input().split())
num  = list(map(int, input().split()))
count = 0
res = []

def recur(start):
  global count
  if sum(res) == S and len(res) > 0:
    count +=1 # 여기에서 return을 해주면 안된다


  for i in range(start, N):
    res.append(num[i])
    recur(i + 1)
    res.pop()

recur(0)
print(count)