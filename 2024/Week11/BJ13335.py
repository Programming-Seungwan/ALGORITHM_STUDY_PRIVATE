from collections import deque

n, w, L = map(int, input().split())
cars = list(map(int, input().split()))

q = deque()
for _ in range(w):
    q.append(0)

time = 0


idx = 0
while idx < n:
    time += 1
    q.popleft()


    if sum(q)+cars[idx] <= L:
        q.append(cars[idx])
        idx += 1

    else:
        q.append(0)

while q:
    time += 1
    q.popleft()

print(time)