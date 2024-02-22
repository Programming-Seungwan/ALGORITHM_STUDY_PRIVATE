from sys import stdin as s
s = open('./input.txt', 'rt')

n, goal = list(map(int, s.readline().strip().split()))
coinList = []
for _ in range(n):
  coinList.append(int(s.readline()))
coinList.sort()

dp = [0 for _ in range(goal + 1)]
dp[0] = 1

# 같은 조합인데, 순서가 달라서 중복이 발생하는 경우가 있다 => 사용하는 동전의 순서를 정해준다.
# 이는 1을 사용한 다음에 2를 사용하는것이지, 1을 사용하고 2를 사용하는데 다시 1을 사용할 수는 없다는 의미이다

for c in coinList: # 사용할 수 있는 동전의 범위를 늘려가는 것이다.
    for i in range(c, goal + 1): # i가 거쳐가는 모든 것을 동전의 범위를 늘려가면서 매번 갱신한다
       dp[i] = dp[i] + dp[i - c]
print(dp[goal])