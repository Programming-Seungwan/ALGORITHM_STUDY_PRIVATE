function FloydWarshall(graph) {
  // 일단 2차원 배열을 무한대로 채워넣기
  const INF = Number.MAX_SAFE_INTEGER;
  const LENGTH = graph.length;
  const distance = new Array(LENGTH)
    .fill(null)
    .map(() => new Array(LENGTH).fill(INF));

  // graph에 있는 정보로 초기화

  for (let i = 0; i < LENGTH; i++) {
    for (let j = 0; j < LENGTH; j++) {
      if (i === j) {
        distance[i][j] = 0;
      } else if (graph[i][j] !== 0) {
        distance[i][j] = graph[i][j];
      }
    }
  }

  for (let k = 0; k < LENGTH; k++) {
    for (let i = 0; i < LENGTH; i++) {
      for (let j = 0; j < LENGTH; j++) {
        if (distance[i][j] > distance[i][k] + distance[k][j]) {
          distance[i][j] = distance[i][k] + distance[k][j];
        }
      }
    }
  }

  return distance;
}

const graph = [
  [0, 2, 4, 0, 0],
  [0, 0, 1, 7, 0],
  [6, 0, 0, 0, 5],
  [0, 0, 8, 0, 3],
  [0, 0, 0, 0, 0],
];

const result = FloydWarshall(graph);
console.log(result);
