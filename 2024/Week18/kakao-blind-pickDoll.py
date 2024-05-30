# 정방 행렬을 뒤집은 행렬을 반환하는 함수
def getReversedMatrix(mtx):
  n = len(mtx)
  returnMtx = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      returnMtx[i][j] = mtx[j][i]

  return returnMtx



def solution(board, moves):
    answer = 0
    n = len(board)
    dollMtx = getReversedMatrix(board)
    stack = []
    # moves를 순회하면서
    for move in moves:
       for i in range(n):
          if (dollMtx[move - 1][i] != 0):
             stack.append(dollMtx[move - 1][i])
             dollMtx[move - 1][i] = 0
             stackLen = len(stack)
             if ((stack[stackLen - 1] == stack[stackLen - 2]) and stackLen >=2):
                stack.pop()
                stack.pop()
                answer += 2
             break

    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))