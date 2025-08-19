const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', (line) => {
  input.push(line.trim());
}).on('close', () => {
  const [n, m] = input[0].split(' ').map(Number);
  const commands = input.slice(1).map((line) => line.split(' ').map(Number));

  class UnionFind {
    constructor(size) {
      this.parent = Array.from({ length: size }, (_, i) => i);
      this.rank = Array(size).fill(1);
    }

    find(x) {
      if (this.parent[x] !== x) {
        this.parent[x] = this.find(this.parent[x]);
      }
      return this.parent[x];
    }

    union(x, y) {
      const rootX = this.find(x);
      const rootY = this.find(y);

      if (rootX === rootY) return false; // Already in the same set

      // Union by rank
      if (this.rank[rootX] < this.rank[rootY]) {
        this.parent[rootX] = rootY;
      } else if (this.rank[rootX] > this.rank[rootY]) {
        this.parent[rootY] = rootX;
      } else {
        this.parent[rootY] = rootX;
        this.rank[rootX] += 1;
      }
      return true;
    }

    isInSameGroup(x, y) {
      return this.find(x) === this.find(y);
    }
  }

  const uf = new UnionFind(n);
  let output = [];
  for (const command of commands) {
    const [c, x, y] = command;
    if (c === 0) {
      uf.union(x, y);
    } else {
      output.push(uf.isInSameGroup(x, y) ? 'YES' : 'NO');
    }
  }
  console.log(output.join('\n'));
});

// ...기존 코드 삭제, readline 내부로 이동...
