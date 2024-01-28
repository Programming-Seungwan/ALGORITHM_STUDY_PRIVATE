from sys import stdin as s
from itertools import combinations

s= open('./input.txt', 'rt')
# 6개를 합쳐야됨

res = []

def recur(start, inputArray, maxNum):
  res.append(inputArray[start])

  if len(res) == 6:
    for k in range(6):
      print(res[k], end=" ")
    print(end='\n')
    return

  for j in range(start + 1, maxNum):
    recur(j, inputArray, maxNum)
    res.pop()


while True:
  tmpLine = s.readline().strip()
  if tmpLine == '0':
    break
  totalLine = list(map(int, tmpLine.split()))
  length = totalLine[0]
  elements = []
  for i in range(1, length + 1):
    elements.append(totalLine[i])
  # print(elements)
  for m in range(0, length - 6 + 1):
    recur(m, elements, length )
    res = []
  print(end='\n')
