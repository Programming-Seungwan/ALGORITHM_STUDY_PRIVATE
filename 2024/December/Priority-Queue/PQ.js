// 우선 순위 큐 구현 in Javascript
class PriorityQueue {
  constructor() {
    this.queue = []; // 큐 자체는 사실 배열에 불과함
  }

  enqueue(element, priority) {
    const queueElement = { element, priority };

    let added = false; // flag 변수에 해당함

    for (let i = 0; i < this.queue.length; i++) {
      if (queueElement.priority < this.enqueue[i].priority) {
        this.queue.splice(i, 0, queueElement);
        added = true;
        break; // 이미 우선 순위 큐는 정렬되어 있는 것이기 때문에 빠져나가도 됨
      }
    }

    // 위의 반복문을 돌면서 어느 것에도 해당되지 않는 경우에 queue 배열의 가장 마지막에 밀어넣기
    if (!added) {
      this.queue.push(queueElement);
    }
  }

  isEmpty() {
    return this.queue.length === 0;
  }

  dequeue() {
    if (this.queue.isEmpty()) {
      return 'Queue is Empty';
    }

    return this.queue.shift(); // 가장 첫번째 요소를 반환한다
  }

  peek() {
    if (this.queue.length === 0) {
      return 'Queue is Empty';
    }

    return this.queue[0];
  }

  size() {
    return this.queue.length;
  }
}
