# 아이디어 : for문 안에서 재귀함수를 돌린다. 재귀함수 다음의 코드에는 다시 방문이 가능하도록 만들어주는 것 필요
# 필요한 자료 구조 : 결과를 출력할 res 리스트, 체크를 기록할 리스트
from sys import stdin as s

s = open('./input.txt', 'rt')

N, M = list(map(int, s.readline().strip().split(' ')))

res = []
check = [False] * (N + 1)

# 재귀함수의 인자가 목표로 하는 수열의 길이와 같으면 출력하고 함수를 종료시킨다
def recur(num):
  if num == M:
    print(' '.join(map(str, res)))
    return
  # for 문을 돌리기
  for i in range(1, N + 1):
    check[i] = True
    res.append(i)
    recur(num + 1)
    check[i] = False
    res.pop()

recur(0)