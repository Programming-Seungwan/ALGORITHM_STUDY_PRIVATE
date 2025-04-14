from sys import stdin as s
s = open('./input.txt', 'rt')

[N, K] = list(map(int, s.readline().strip().split()))
# N은 합을 의미하고, K는 슬라이딩 윈도우의 길이를 의미한다.
# 어디까지인지 한계를 지어줄 필요가 있음. N-1까지면 됨
originalList = [i for i in range(N)]
accSumList = [0 for _ in range(N)]

for i in range(1, N):
  accSumList[i] = accSumList[i -1] + originalList[i]

flag = False
for i in range(K, N):
  tmpSum = accSumList[i] - accSumList[i - K]
  if tmpSum == N:
    print(originalList[i] - originalList[i - K + 1])
    flag = True
    break

if flag == False:
  print(-1)