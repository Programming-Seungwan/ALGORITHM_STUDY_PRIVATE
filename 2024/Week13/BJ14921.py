import sys

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))

    left, right = 0, N - 1
    ans = arr[left] + arr[right]
    while left < right:
        tmp = arr[left] + arr[right]
        if abs(ans) > abs(tmp):
            ans = tmp
        if tmp < 0: left += 1
        else: right -= 1
    print(ans)