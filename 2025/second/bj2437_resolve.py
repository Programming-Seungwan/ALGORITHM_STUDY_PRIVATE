# 연속적인 그래프를 이용해서 푸는 것임. 기존의 ㄱㄴ 집합에서는 연속적인 것들이 다 가능했음.
# 즉, 무언가를 자유롭게 하나 뺄수 있다는 것임. 따라서 특정 구간까지의 합이 가능했다면 추가되는 추에의한 값까지도 모두 가능함. 왜냐? 그 사이의 것들은 기존 최대값에서 뺀 것이 가능하기 때문이다.
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1 # 처음에는 1을 겨냥한다.

for num in arr:
    if target < num:
        break

    target += num # target을 갱신해나간다.

print(target)