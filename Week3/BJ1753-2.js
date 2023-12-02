// 우선 순위 큐를 사용하지 않고 다익스트라 알고리즘을 구현한 사례

const fs = require('fs');
const { start } = require('repl');
let arr = fs.readFileSync('./input.txt').toString().trim().split('\n');

arr = arr.map((v) => {
  return v.split(' ').map((n) => parseInt(n));
});

// V는 정점, E는 감선의 개수이고 startIndex는 시작 정점을 의미. graphArray는 간선 간의 가중치를 의미
const [[V, E], [startVertex], ...graphArray] = arr;

class Graph {
  constructor() {
    this.nodes = [];
    this.edges = {};
  }

  addNode(node1) {
    this.nodes.push(node1);
    this.edges[node1] = [];
  }

  addEdge(node1, node2, weight) {
    this.edges[node1].push({ node: node2, weight: weight });
  }

  dijkstra(startNode) {
    // 우선 각 노드까지의 거리를 모두 무한대로 만들어주어야 함
    // 시작점부터 각 노드까지의 거리가 얼마인지를 저장할 배열
    const distances = {};
    // 각 노드가 방문된 적이 있는지를 나타내는 객체
    const visited = {};
    const { nodes, edges } = this;

    nodes.forEach((node) => {
      // 모든 정점까지의 거리는 무한대, 방문 여부는 false로 초기화 해준다
      distances[node] = Infinity;
      visited[node] = false;
    });

    // 여기에서 자기 자신을 방문 true 처리해버리면 for문을 돌 수가 없음
    distances[startNode] = 0;

    // 전체를 돌면서 자기 자신을 제외한 횟수만큼 갱신화를 진행
    for (let i = 0; i < nodes.length - 1; i++) {
      const currentNode = this.getMinCostNode(distances, visited);

      visited[currentNode] = true;

      edges[currentNode].forEach((neighbor) => {
        const tmpDistance = distances[currentNode] + neighbor.weight;

        if (tmpDistance < distances[neighbor.node]) {
          distances[neighbor.node] = tmpDistance;
        }
      });
    }

    return distances;
  }

  // 아직 방문하지 않았고 비용이 가장 작은 노드를 반환하는 함수 => 원래 이것을 minHeap로 구현하는 것이 맞음
  getMinCostNode(tmpDistances, tmpVisited) {
    // distances 객체에 있는 노드들을 싹 뽑아줌
    let myNodes = Object.keys(tmpDistances);

    // console.log(myNodes);
    myNodes = myNodes.filter((node) => !tmpVisited[node]);

    return myNodes.reduce((min, node) => (tmpDistances[node] < tmpDistances[min] ? node : min), myNodes[0]);
  }
}

const graph = new Graph();

for (let i = 0; i < V; i++) {
  graph.addNode(i + 1);
}

for (let i = 0; i < E; i++) {
  graph.addEdge(graphArray[i][0], graphArray[i][1], graphArray[i][2]);
}

const result = graph.dijkstra(startVertex);

for (let i = 1; i <= V; i++) {
  if (result[i] === Infinity) {
    console.log('INF');
    continue;
  }
  console.log(result[i]);
}
