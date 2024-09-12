const fs = require('fs');
const filepath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const [n, ...arr] = fs.readFileSync(filepath).toString().trim().split('\n');
const realArr = arr.map((el) => +el);

class MinHeap {
  constructor() {
    this.heap = [];
  }

  push(value) {
    this.heap.push(value);
    this.heapifyUp();
  }

  pop() {
    if (this.isEmpty()) return null;

    const root = this.heap[0];
    const lastNode = this.heap.pop();

    if (!this.isEmpty()) {
      this.heap[0] = lastNode;
      this.heapifyDown();
    }

    return root;
  }

  isEmpty() {
    return this.heap.length === 0;
  }

  heapifyUp() {
    let index = this.heap.length - 1;
    while (index > 0) {
      const parentIndex = Math.floor((index - 1) / 2);
      if (this.heap[parentIndex] <= this.heap[index]) break;
      [this.heap[parentIndex], this.heap[index]] = [
        this.heap[index],
        this.heap[parentIndex],
      ];
      index = parentIndex;
    }
  }

  heapifyDown() {
    let index = 0;
    const length = this.heap.length;

    while (true) {
      let smallest = index;
      const leftChildIndex = 2 * index + 1;
      const rightChildIndex = 2 * index + 2;

      if (
        leftChildIndex < length &&
        this.heap[leftChildIndex] < this.heap[smallest]
      ) {
        smallest = leftChildIndex;
      }

      if (
        rightChildIndex < length &&
        this.heap[rightChildIndex] < this.heap[smallest]
      ) {
        smallest = rightChildIndex;
      }

      if (smallest === index) break;

      [this.heap[index], this.heap[smallest]] = [
        this.heap[smallest],
        this.heap[index],
      ];
      index = smallest;
    }
  }
}

if (realArr.length === 1) {
  console.log(0);
} else {
  // min Heap이 빌때까지 알고리즘을 진행함
  let resultSum = 0; // 결과로 반환할 값을 의미함

  const hp = new MinHeap();

  for (const realArrElement of realArr) {
    hp.push(realArrElement);
  }

  while (!hp.isEmpty()) {
    if (hp.heap.length === 1) {
      resultSum += hp.pop();
      break;
    } else if (hp.heap.length === 2) {
      resultSum += hp.pop() + hp.pop();
      break;
    }

    const mostSmallNumberInHeap = hp.pop();
    const secondSmallNumberInHeap = hp.pop();

    const tmpSum = mostSmallNumberInHeap + secondSmallNumberInHeap;
    resultSum += tmpSum;
    hp.push(tmpSum);
  }

  console.log(resultSum);
}
