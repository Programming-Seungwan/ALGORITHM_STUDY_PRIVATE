def team(a,n):
    global result
    if a == N//2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += S[i][j]
                elif not visited[i] and not visited[j]:
                    link +=S[i][j]
        result = min(result,abs(start-link))
        return
    else :
        for x in range(n,N):
            if visited[x] == 0:
                visited[x] = 1
                team(a+1,x+1)
                visited[x] = 0
import sys
N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [0]*N
result = float('inf')
team(0,0)
print(result)
