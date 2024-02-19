def solution(m, n, puddles):
    revisedPuddles = [[q, p] for [p, q] in puddles] # x와 y 좌표가 거꾸로 되어 있음
    memo = [[0] * (m + 1) for _ in range(n + 1)]
    memo[1][1] = 1
    for j in range(1, n + 1):
        for i in range(1, m+ 1):
            if i == 1 and j == 1: continue # 출발점의 경우에는 다시 기록하지 않음
            elif [j, i ] in revisedPuddles: # 웅덩이에 해당하는경우
                memo[j][i] = 0
            else:
                memo[j][i] = memo[j - 1][i] + memo[j][i - 1] # 위와 아래에서 오는 경우를 의미함 경우는 두가지 뿐

    return memo[n][m] % 1000000007

print(solution(4, 3, [[2, 2]]))