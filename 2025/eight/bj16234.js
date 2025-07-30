const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';

// Read from input.txt for local testing
const [firstLine, ...restArr] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split('\n');

const [N, L, R] = firstLine.split(' ').map(Number);
let board = restArr.map((row) => row.split(' ').map(Number)); // 함수형 프로그래밍을 많이 사용함

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

let days = 0;

while (true) {
  const visited = Array.from({ length: N }, () => Array(N).fill(false));
  let isMoved = false;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (!visited[i][j]) {
        const queue = [[i, j]];
        const union = [[i, j]];
        let sum = board[i][j];
        visited[i][j] = true;

        let head = 0;
        while (head < queue.length) {
          const [x, y] = queue[head++];

          for (let k = 0; k < 4; k++) {
            const nx = x + dx[k];
            const ny = y + dy[k];

            if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny]) {
              const diff = Math.abs(board[x][y] - board[nx][ny]);
              if (diff >= L && diff <= R) {
                visited[nx][ny] = true;
                queue.push([nx, ny]);
                union.push([nx, ny]);
                sum += board[nx][ny];
              }
            }
          }
        }

        if (union.length > 1) {
          isMoved = true;
          const avg = Math.floor(sum / union.length);
          for (const [ux, uy] of union) {
            board[ux][uy] = avg;
          }
        }
      }
    }
  }

  if (!isMoved) {
    break;
  }
  days++;
}

console.log(days);
