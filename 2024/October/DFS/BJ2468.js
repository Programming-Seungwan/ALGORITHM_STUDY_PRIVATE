const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');
const N = +input[0];
const areas = input.slice(1).map((v) => v.split(' ').map((v) => +v));

const offsetX = [0, 0, -1, 1];
const offsetY = [-1, 1, 0, 0];

const dfs = (x, y, height, visited) => {
  offsetX.forEach((dx, i) => {
    const nx = x + dx;
    const ny = y + offsetY[i];
    if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny]) {
      visited[nx][ny] = true;
      dfs(nx, ny, height, visited);
    }
  });
};

let maxCount = 0;
for (let height = 0; height <= 100; height++) {
  let count = 0;
  const visited = [...Array(N)].map((_, x) =>
    [...Array(N)].map((_, y) => areas[x][y] <= height)
  );
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (!visited[i][j]) {
        visited[i][j] = true;
        dfs(i, j, height, visited);
        count++;
      }
    }
  }
  maxCount = Math.max(maxCount, count);
}

console.log(maxCount);
