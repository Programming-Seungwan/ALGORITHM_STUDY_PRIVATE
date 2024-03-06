from sys import stdin as s
s = open('./input.txt', 'rt')
n = int(s.readline().strip())
memo = [0 for _ in range(n + 1)]
time = [0]
price = [0]
for _ in range(n):
  t, p = list(map(int, s.readline().strip().split()))
  time.append(t)
  price.append(p)

for i in range(1, n + 1):
  memoIndex = i + time[i] - 1 # 새로 기록할 숫자에 해당함. n을 넘어가면 쓸 수 없음
  if memoIndex > n: continue
  else:
    beforeMax = max(memo[0:i]) # 한 칸 이전의 수치에서 새롭게 받을 급여를 더하는 것이 아니라, 이전 memo 중에서 가장 큰 것을 선택하는 것이 포인트. 중간에 그냥 나중을 위해서 쉬는 것이 유리할 수도 있기 떄문임
    if (beforeMax + price[i]) >= memo[memoIndex]:
      memo[memoIndex] = beforeMax + price[i]

print(max(memo))