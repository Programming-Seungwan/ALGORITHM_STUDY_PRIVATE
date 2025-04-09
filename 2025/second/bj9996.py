from sys import stdin as s

s = open('./input.txt', 'rt')
# 별표가 패턴의 맨앞, 중간, 맨끝에 위치한 경우를 모두 고려해야함

# 맨 앞에 있는 경우 -> 별표 다음의 것을 get하고, 들어 있는지를 파악한다.
# 중간에 있는 경우 -> 별표 앞의 것이 있는지를 겟하고, 뒤의 것도 겟 한뒤, 둘다 있는지를 확인하고 앞의것이 더 우선하는지를 확인한다.
# 맨 뒤에 있는 경우 -> 별표 앞의 것을 get하고, 들어 있는지를 파악한다.
# 파이썬에서 인덱스를 찾아주는 메서드는 find()임. 없으면 -1을 반환함

N = int(s.readline().strip())
pattern = s.readline().strip()
patternLength = len(pattern)
fileNameList = [s.readline().strip() for _ in range(N)]



def process(fileName):
  asteriskIndex = pattern.find('*')
  # 별표가 맨 뒤에 있는 경우
  if (asteriskIndex == patternLength - 1):
    findingString = pattern[0 : patternLength - 1]
    findingStringIndex = fileName.find(findingString)

    if (findingStringIndex == -1):
      print('NE')
    else:
      print('DA')

    return
  # 별표가 맨 앞에 있는 경우
  if (asteriskIndex == 0):
    findingString = pattern[1 : patternLength]
    findingStringIndex = fileName.find(findingStringIndex)
    if (findingStringIndex == -1):
      print('NE')
    else:
      print('DA')
    return

  firstFindingString = pattern[0 : asteriskIndex]
  secondFindingString = pattern[asteriskIndex + 1 : ]

  firstFindingIndex = fileName.find(firstFindingString)
  secondFindingIndex = fileName.find(secondFindingString)

  if (firstFindingIndex != -1 and secondFindingIndex != -1 and firstFindingIndex < secondFindingIndex):
    print('DA')
  else:
    print('NE')

for fn in fileNameList:
  process(fn)