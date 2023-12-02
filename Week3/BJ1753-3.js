// 우선 순위 큐를 구현하여 푼 풀이 2
const input = require('fs').readFileSync('dev/stdin').toString().trim().split('\n');

// 우선 순위 큐를 만들어줌
class PQ {
  // 우선 순위를 지정할 기준 함수를 생성자의 인자로 받는다

  constructor(calc) {
    this.comp = calc;
    this.heap = [];
  }

  push(v) {
    this.heap.push(v);

    let cur = this.heap.length - 1;

    while (cur > 0) {
      let parent = Math.floor((cur - 1) / 2);

      if (this.comp(this.heap[cur], this.heap[parent]) <= 0) break;

      this.swap(cur, parent);
      cur = parent;
    }
  }

  pop() {
    if (this.heap.length === 1) return this.heap.pop();

    const peek = this.heap[0];
    this.heap[0] = this.heap.pop();
    const size = this.heap.length;

    let cur = 0;

    while (cur < size) {
      let parent = cur;
      let left = cur * 2 + 1;
      let right = cur * 2 + 2;

      if (left < size && this.comp(this.heap[left], this.heap[parent]) >= 0) parent = left;
      if (right < size && this.comp(this.heap[right], this.heap[parent]) >= 0) parent = right;
      if (parent === cur) break;

      this.swap(cur, parent);
      cur = parent;
    }
    return peek;
  }

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }
}

const [v, e] = input[0].split(' ').map(Number);
const k = Number(input[1]);
const graph = Array.from({ length: v + 1 }, () => []);

for (let i = 2; i < e + 2; i++) {
  const [a, b, c] = input[i].split(' ').map(Number);
  graph[a].push([b, c]);
}
// console.log(graph);

const INF = 1e9;
const dp = new Array(v + 1).fill(INF);

function dijkstra(start) {
  const pq = new PQ((a, b) => b[1] - a[1]);
  pq.push([start, 0]);
  dp[start] = 0;

  while (pq.heap.length) {
    const [cur, cost] = pq.pop();

    for (const [next, nCost] of graph[cur]) {
      const dist = nCost + cost;

      if (dist < dp[next]) {
        pq.push([next, dist]);
        dp[next] = dist;
      }
    }
  }
}

dijkstra(k);

const ans = [];
for (let i = 1; i <= v; i++) dp[i] === INF ? ans.push('INF') : ans.push(dp[i]);
console.log(ans.join('\n'));
