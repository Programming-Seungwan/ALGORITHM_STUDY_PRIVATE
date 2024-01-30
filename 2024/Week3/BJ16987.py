n = int(input())
s = [0]*n # 내구도와 무게를 각기 다른 배열에 저장함
w = [0]*n

for i in range(n):
    s[i], w[i] = map(int, input().split())

res = 0
# 손에 든 계란의 인덱스와 계란의 내구도 배열을 인자로 받음
def solve(idx, eggs):
    global res # 가장 많이 깬 계란의 개수를 저장할 전역 변수에 해당함
    if idx == n:
        cnt = 0
        for i in range(n):
            if eggs[i] <= 0: # 깨진 계란의 수를 카운팅
                cnt +=1
        if cnt > res:
            res = cnt
        return

    if eggs[idx] > 0: # 손에 든 계란이 깨지지 않은 경우를 의미함
        for i in range(n):
            flag = False # 파이썬에서는 함수 내 for문에서 변수를 선언해도 유효 범위가 함수임
            if eggs[i] > 0 and i != idx: # 아직 안 깨진 계란이면서 손에 든 계란이 아닌 계란
                flag = True
                tmp = eggs[:]
                tmp[i] -= w[idx]
                tmp[idx] -= w[i]
                solve(idx+1, tmp)

        if not flag:
            solve(idx+1, eggs)
    else:
        solve(idx+1, eggs) # 손에 든 계란 자체가 깨져있는 경우에 다음 계란으로 진행함

solve(0, s)
print(res)