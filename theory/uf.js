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

  findParent(x, y) {
    return this.find(x) === this.find(y);
  }

  union(x, y) {
    const rootX = this.find(x);
    const rootY = this.find(y);

    if (rootX < rootY) {
      this.parent[rootY] = rootX;
    } else if (rootX > rootY) {
      this.parent[rootX] = rootY;
    }
  }
}
