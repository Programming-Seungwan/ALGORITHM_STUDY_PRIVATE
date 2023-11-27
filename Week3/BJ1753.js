// 백준 1753 최단 거리 경로 문제입니다.
//https://www.acmicpc.net/problem/1753

const fs = require('fs');
let arr = fs.readFileSync('./input.txt').toString().trim().split('\n');

arr = arr.map((v) => {
  return v.split(' ').map((n) => parseInt(n));
});

// V는 정점, E는 감선의 개수이고 startIndex는 시작 정점을 의미. graphArray는 간선 간의 가중치를 의미
const [[V, E], [startVertex], ...graphArray] = arr;

class PriorityQueue {
  constructor() {
    this.queue = [];
  }

  enqueue(element, priority) {
    // element는 노드, priority는 간선의 가중치를 나타냄
    this.queue.push({ element, priority });
    // 우선 순위 큐에 넣어준 다음에는 오름차순으로 정렬해준다
    this.sortQueue();
  }

  dequeue() {
    return this.queue.shift();
  }

  sortQueue() {
    this.queue.sort((a, b) => a.priority - b.priority);
  }

  isEmpty() {
    return this.queue.length === 0;
  }
}

class Graph {
  constructor() {
    this.nodes = [];
    this.edges = {};
  }

  addNode(someNode) {
    this.nodes.push(someNode);
    this.edges[someNode] = [];
  }

  addEdge(node1, node2, weight) {
    this.edges[node1].push({ node: node2, weight: weight });
  }

  dijkstra(stNode) {
    // 반환할 결과, 즉 모든 정점으로의 최단 거리를 담은 객체이다
    const distances = {};
    const visited = {};
    const pq = new PriorityQueue();

    this.nodes.forEach((node) => {
      distances[node] = Infinity;
      visited[node] = false;
    });
    distances[stNode] = 0;
    pq.enqueue(stNode, 0);

    while (!pq.isEmpty()) {
      const { element: currentNode, priority: currentDistance } = pq.dequeue();
      if (visited[currentNode]) continue;
      visited[currentNode] = true;

      this.edges[currentNode].forEach((neighbor) => {
        const distance = currentDistance + neighbor.weight;
        if (distance < distances[neighbor.node]) {
          distances[neighbor.node] = distance;
          pq.enqueue(neighbor.node, distance);
        }
      });
    }
    return distances;
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

for (const a in result) {
  if (result[a] === Infinity) {
    console.log('INF');
    continue;
  }
  console.log(result[a]);
}
