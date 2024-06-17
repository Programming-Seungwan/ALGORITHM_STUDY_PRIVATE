# 자료구조 : 재귀, 혹은 스택을 이용한 dfs 알고리즘, visited 배열을 통해 해당 지점이 방문한 곳인지를 탐색하기
# 필요 함수 : 특정 지점으로부터 특정 방향으로 가게되면 도착하는 위치 좌표를 반환하는 함수 : 배열, 시작 위치 x, y가 인자로 들어옴
# 논리 구조
# 1. 특정 지점에서 상하 좌우로 가게 되면 갈 수 있는 좌표가 이미 방문한 곳인지를 확인 : 이미 방문한 곳이라면 다시 가봐야 레파토리가 반복되니까
# 2. 갈 수가 있는 곳이라면 이동시키고 현재 좌표를 수정하고 이동 횟수를 하나 늘리기. 재귀 함수가 끝난 뒤에는 다시 해당 좌표를 false로 바꿔주기
example = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]

directions = ['u', 'r', 'd', 'l'] # 상하좌우를 나타내는 배열

def getDestination(currentX, currentY, board, direction): # 다음 위치를 반환하는 함수에 해당
    rowLength = len(board)
    colLength = len(board[0])
    if (direction == 'u'):
        while(board[currentX][currentY] != 'D' and (currentX >= 0)):
            if ((currentX - 1 >= 0) and board[currentX -1][currentY] != 'D'):
                currentX -= 1
            else:
                break
        return [currentX, currentY]
    elif (direction == 'r'):
        while(board[currentX][currentY] != 'D' and (currentY < colLength)):
            if ((currentY + 1 < colLength) and board[currentX][currentY + 1] != 'D'):
                currentY += 1
            else:
                break
        return [currentX, currentY]
    elif (direction == 'd'):
        while(board[currentX][currentY] != 'D' and (currentX < rowLength)):
            if ((currentX + 1 < rowLength) and board[currentX + 1][currentY] != 'D'):
                currentX += 1
            else:
                break
        return [currentX, currentY]
    elif (direction == 'l'):
        while(board[currentX][currentY] != 'D' and (currentX < rowLength)):
            if ((currentY - 1 >= 0) and board[currentX][currentY - 1] != 'D'):
                currentY -= 1
            else:
                break
        return [currentX, currentY]
crtX = 0
crtY = 0

def solution(board):
    global crtX, crtY
    resultArray = []
    answer = 0
    count = 0
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    rowLength, colLength = [len(board), len(board[0])]
    boardMtx = [list(s) for s in board] # board를 행렬로 만든 것
    for i in range(rowLength):
        for j in range(colLength):
            if boardMtx[i][j] == 'R':
                visited[i][j] = True
                crtX = j
                crtY = i
    
    for direction in directions:
        resultPositionX, resultPositonY = getDestination(crtX, crtY, boardMtx, direction)
        if (visited[resultPositionX][resultPositonY] != True):
            count += 1
            if (visited[resultPositionX][resultPositonY] == 'G'):
                resultArray.append(count)
            
                

              



    print(visited)
    return answer

# solution(example)