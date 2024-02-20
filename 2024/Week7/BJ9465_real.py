import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    # 2행 DP배열 형성
    DP = [[0] * N for _ in range(2)]

    # 스티커 길이가 1일 경우
    DP[0][0] = arr[0][0]
    DP[1][0] = arr[1][0]
    if N == 1:
        print(max(DP[0][0], DP[1][0]))
        continue

    # 스티커 길이가 2일 경우
    DP[0][1] = arr[1][0] + arr[0][1]
    DP[1][1] = arr[0][0] + arr[1][1]
    if N == 2:
        print(max(DP[0][1], DP[1][1]))
        continue

    # 스티커 길이가 3이상일 경우
    for i in range(2, N):
        # 메인 아이디어 => 윗칸 기준으로 할지, 아랫칸 기준으로 할지 모두 적용해줌
        DP[0][i] = max(DP[1][i - 2], DP[1][i - 1]) + arr[0][i] #전자는 하나의 열 건너뛴 것, 후자는 포함시킨 것
        DP[1][i] = max(DP[0][i - 2], DP[0][i - 1]) + arr[1][i]

    print(max(DP[0][-1], DP[1][-1]))