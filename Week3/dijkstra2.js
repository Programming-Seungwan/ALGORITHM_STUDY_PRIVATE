// 우선 순위 큐를 이용하여 구현한 다익스트라 알고리즘
class PriorityQueue {
  constructor() {
    this.queue = [];
  }

  enqueue(element, priority) {
    this.queue.push({ element, priority });
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

  addNode(node) {
    this.nodes.push(node);
    this.edges[node] = [];
  }

  addEdge(node1, node2, weight) {
    this.edges[node1].push({ node: node2, weight: weight });
    this.edges[node2].push({ node: node1, weight: weight });
  }

  dijkstra(startNode) {
    const distances = {};
    const visited = {};
    const pq = new PriorityQueue();

    // 초기화
    this.nodes.forEach((node) => {
      distances[node] = Infinity;
      visited[node] = false;
    });
    distances[startNode] = 0;
    pq.enqueue(startNode, 0);

    // 다익스트라 알고리즘
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

// 예제
const graph = new Graph();

graph.addNode('A');
graph.addNode('B');
graph.addNode('C');
graph.addNode('D');
graph.addNode('E');

graph.addEdge('A', 'B', 1);
graph.addEdge('A', 'C', 4);
graph.addEdge('B', 'C', 2);
graph.addEdge('B', 'D', 5);
graph.addEdge('C', 'D', 1);
graph.addEdge('D', 'E', 7);

const startNode = 'A';
const result = graph.dijkstra(startNode);

console.log(`Shortest distances from ${startNode}:`, result);
