// 해당 소스 코드는 Javascript class를 이용하여 구현한 다익스트라 알고리즘입니다.

class Graph {
  constructor() {
    this.nodes = [];
    this.edges = {};
  }

  addNode(someNode) {
    this.nodes.push(someNode);
    // 객체의 속성으로서 배열을 할당. 해당 배열의 원소는 연결되는 노드에 대한 간선 가중치를 담은 객체들임. 필드는 node와 weight
    this.edges[someNode] = [];
  }

  addEdge(node1, node2, weight) {
    this.edges[node1].push({ node: node2, weight: weight });
    this.edges[node2].push({ node: node1, weight: weight });
  }

  // 시작점으로부터 다른 노드들까지의 최단 거리를 반환해주는 함수
  dijkstra(startNode) {
    const distances = {};
    const visited = {};
    // 해당 클래스에 속하는 nodes 배열과 edges 객체를 구조 분해 방식으로 받기
    const { nodes, edges } = this;

    nodes.forEach((node) => {
      // 출발점으로부터 해당 node까지의 거리는 일단 무한대로 초기화
      distances[node] = Infinity;
      // 아직 모든 node들은 방문된 것이 아님
      visited[node] = false;
    });
    distances[startNode] = 0;

    for (let i = 0; i < nodes.length - 1; i++) {
      const currentNode = this.minDistanceNode(distances, visited);
      visited[currentNode] = true;

      edges[currentNode].forEach((nearbynode) => {
        const tmpDistance = distances[currentNode] + nearbynode.weight;

        if (tmpDistance < distances[nearbynode.node]) {
          distances[nearbynode.node] = tmpDistance;
        }
      });
    }

    return distances;
  }

  // 시작 노드로부터 가장 거리가 가까운 노드를 구하는 함수
  // distances는 시작점으로부터의 거리를 담은 객체임
  minDistanceNode(distances, visited) {
    // 우선 A로부터의 거리가 기록된 모든 정점들을 모은다
    const nodes = Object.keys(distances);

    return nodes.reduce((min, node) => {
      if (!visited[node] && distances[node] < distances[min]) {
        return node;
      } else {
        return min;
      }
    }, nodes[0]);
  }
}

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
