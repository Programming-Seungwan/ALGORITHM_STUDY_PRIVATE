from sys import stdin as s

s = open('./input.txt', 'rt')

# stack 자료구조를 이용하는 문제임.
# 레이저를 그냥 2칸짜리라고 생각하면 되려나? 어차피 레이저는 (n, n+1)이다. 즉, n이 막대기의 시작점보다 오른쪽이면 내부에 있는 것이다.
# 새로 들어온 것이 ) 이고, 스택의 가장 위의 것이 ( 이면 레이저이고 -> )의 인덱스와 (의 인덱스가 1차이일때
# [요소, 요소의 인덱스] 방식으로 저장한다.
# ) 와 (의 인덱스 차이가 1 이상이면 각각 막대의 시작 인덱스와 종료 인덱스이다.

layout = list(s.readline().strip())

stack = []
stack.append([layout[0], 0])
lasers = []
pipes = []

for i in range(1, len(layout)):
  newInput = layout[i]

  if (len(stack) == 0):
    stack.append([newInput, i])
    continue
  # 무언가가 있을 때
  if (newInput == ')' and stack[-1][0] == '('):
    if (i - stack[-1][1] == 1):
      poppedItem = stack.pop()
      lasers.append([poppedItem[1], i])
    else:
      poppedItem = stack.pop()
      pipes.append([poppedItem[1], i])

  if (newInput == '('):
    stack.append([newInput, i])

totalCount = 0

for pipe in pipes:
  fragmentCount = 1
  for laser in lasers:
    if (laser[0] > pipe[0] and laser[1] < pipe[1]):
      fragmentCount += 1
  totalCount += fragmentCount

print(totalCount)