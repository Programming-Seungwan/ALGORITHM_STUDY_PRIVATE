class MinHeap {
  constructor() {
    this.heap = [];
  }

  // 부모 노드의 인덱스 반환
  parentIndex(index) {
    return Math.floor((index - 1) / 2);
  }

  // 왼쪽 자식 노드의 인덱스 반환
  leftChildIndex(index) {
    return 2 * index + 1;
  }

  // 오른쪽 자식 노드의 인덱스 반환
  rightChildIndex(index) {
    return 2 * index + 2;
  }

  // 두 인덱스의 값을 교환
  swap(index1, index2) {
    [this.heap[index1], this.heap[index2]] = [
      this.heap[index2],
      this.heap[index1],
    ];
  }

  // 요소 추가 (우선순위에 따라 힙 재정렬)
  insert(element) {
    this.heap.push(element);
    this.heapifyUp();
  }

  // 마지막 요소에서부터 시작해 힙을 재정렬 (부모보다 작은 경우 위로 이동)
  heapifyUp() {
    let index = this.heap.length - 1;
    while (index > 0) {
      let parent = this.parentIndex(index);
      if (this.heap[parent].priority > this.heap[index].priority) {
        this.swap(parent, index);
        index = parent;
      } else {
        break;
      }
    }
  }

  // 루트 요소 제거 및 반환 (가장 우선순위가 높은 요소)
  remove() {
    if (this.heap.length === 0) {
      return 'Heap is empty';
    }
    if (this.heap.length === 1) {
      return this.heap.pop();
    }
    const root = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.heapifyDown();
    return root;
  }

  // 루트에서 시작해 힙을 재정렬 (자식보다 큰 경우 아래로 이동)
  heapifyDown() {
    let index = 0;
    while (this.leftChildIndex(index) < this.heap.length) {
      let smallerChildIndex = this.leftChildIndex(index);
      let rightChild = this.rightChildIndex(index);
      if (
        rightChild < this.heap.length &&
        this.heap[rightChild].priority < this.heap[smallerChildIndex].priority
      ) {
        smallerChildIndex = rightChild;
      }
      if (this.heap[index].priority > this.heap[smallerChildIndex].priority) {
        this.swap(index, smallerChildIndex);
        index = smallerChildIndex;
      } else {
        break;
      }
    }
  }

  // 힙의 크기 반환
  size() {
    return this.heap.length;
  }

  // 힙이 비었는지 확인
  isEmpty() {
    return this.heap.length === 0;
  }

  // 힙 출력 (디버깅용)
  printHeap() {
    console.log(
      this.heap.map((item) => `(${item.element}, ${item.priority})`).join(' ')
    );
  }
}
