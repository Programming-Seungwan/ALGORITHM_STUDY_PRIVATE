from sys import stdin as s

s = open('./input.txt', 'rt')
# 파이썬에서 특정 알파벳의 위치를 알려주는 함수
def alphabet_position(letter):
    return ord(letter) - ord('a') + 1
L, C = list(map(int, s.readline().strip().split(' ')))
alphabetList = list(s.readline().strip().split(' '))
alphabetList = sorted(alphabetList, key = alphabet_position) # 입력받은 알파벳 리스트를 정렬


res = []

def isListHaveMoeum(myList):
    if 'a' in myList:
        return True
    if 'e' in myList:
        return True
    if 'i' in myList:
        return True
    if 'o' in myList:
        return True
    if 'u' in myList:
        return True
    return False

def countJaeum(myList):
    myListLength = len(myList)
    count = 0
    for i in range(myListLength):
        if myList[i] not in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

def recur(start):
    if len(res) == L and isListHaveMoeum(res) and countJaeum(res) >= 2:
        print(''.join(map(str, res)))
        return
    for i in range(start, C):
        res.append(alphabetList[i])
        recur(i + 1)
        res.pop()

recur(0)
