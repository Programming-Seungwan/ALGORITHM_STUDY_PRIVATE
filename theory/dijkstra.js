class Graph {
  constructor() {
    this.nodes = [];
    this.edges = {}; // 각 노드에 연결된 노드들을 기록할 배열
  }

  addNode(node) {
    this.nodes.push(node);
    this.edges[node] = [];
  }

  addEdge(node1, node2, weight) {
    this.edges[node1].push({ node: node2, weight });
    this.edges[node2].push({ node: node1, weight });
  }

  minDistanceNode(distances, visited) {
    const nodes = Object.keys(distances);

    return nodes.reduce((min, node) => {
      if (!visited[node] && distances[node] < distances[min]) {
        return node;
      } else {
        return min;
      }
    }, nodes[0]);
  }

  dijkstra(startNode) {
    // 여기에서 핵심 비즈니스 로직은 전개됨
    const distances = {};
    const visited = {};

    const { nodes, edges } = this;

    nodes.forEach((node) => {
      distances[node] = Infinity;
      visited[node] = false;
    });

    distances[startNode] = 0;

    for (let i = 0; i < nodes.length - 1; i++) {
      const currentNode = this.minDistanceNode(distances, visited);
      visited[currentNode] = true;

      edges[currentNode].forEach((neighbor) => {
        const distance = distances[currentNode] + neighbor.weight;

        if (distance < distances[neighbor.node]) {
          distances[neighbor.node] = distance;
        }
      });
    }

    return distances;
  }
}
