const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';

const [first, ...arr] = fs.readFileSync(filePath).toString().trim().split('\n');

const [n, m] = first.split(' ').map((item) => +item);
const commands = arr.map((item) => item.split(' ').map((newItem) => +newItem));

class UnionFind {
  constructor(size) {
    this.parent = Array.from({ length: size }, (_, i) => i);
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

    if (rootX < rootY) {
      this.parent[rootY] = rootX;
      return true;
    } else if (rootX > rootY) {
      this.parent[rootX] = rootY;
      return true;
    } else {
      return false;
    }
  }

  isInSameGroup(x, y) {
    return this.find(x) === this.find(y);
  }
}

const uf = new UnionFind(n);

for (const command of commands) {
  const [c, x, y] = command;
  if (c === 0) {
    uf.union(x, y);
  } else {
    console.log(uf.isInSameGroup(x, y) ? 'YES' : 'NO');
  }
}
