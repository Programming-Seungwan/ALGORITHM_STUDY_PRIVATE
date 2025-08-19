class UnionFind {
  constructor(size) {
    this.parent = Array.from({ length: size }, (_, i) => i);
    this.rank = Array(size).fill(1);
  }

  find(x) {
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]); // Path compression
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

  connected(x, y) {
    return this.find(x) === this.find(y);
  }
}

// 사용 예시
const uf = new UnionFind(10);
console.log(uf);
// uf.union(1, 2);
// uf.union(2, 3);
// console.log(uf.connected(1, 3)); // true
// console.log(uf.connected(1, 4)); // false

module.exports = UnionFind;
