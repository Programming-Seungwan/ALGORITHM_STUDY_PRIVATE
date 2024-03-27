import sys
input = sys.stdin.readline


def canCoordinate(sticker):
    coordinate = []
    yOffset = len(sticker)
    xOffset = len(sticker[0])
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 0 or (maps[y][x] and sticker[0][0] == 0):
                if y + yOffset <= n:
                    if x + xOffset <= m:
                        coordinate.append((y, x))
    return coordinate


def canPut(sticker, y, x):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if maps[i + y][j + x] and sticker[i][j]:
                return False
    return True


def put(sticker, y, x):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j]:
                maps[i + y][j + x] = 1


def rotation(sticker):
    # 회전
    sticker = zip(*sticker[::-1])
    return [list(e) for e in sticker]


def logic(sticker):
    for _ in range(4):
        coordinate = canCoordinate(sticker)
        if coordinate:
            for y, x in coordinate:
                if canPut(sticker, y, x):
                    put(sticker, y, x)
                    return
        sticker = rotation(sticker)


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    maps = [[0] * m for _ in range(n)]
    stickers = []
    for _ in range(k):
        y, x = map(int, input().split())
        sticker = [list(map(int, input().split())) for _ in range(y)]
        stickers.append(sticker)

    for sticker in stickers:
        logic(sticker)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j]:
                cnt += 1
    print(cnt)