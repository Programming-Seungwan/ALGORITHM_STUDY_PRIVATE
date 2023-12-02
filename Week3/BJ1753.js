const fs = require('fs');
const I = fs.readFileSync('./input.txt').toString().trim().split('\n');
// 배열 내의 두 원소를 swap 해주는 기능의 함수
const swap = (A, a, b) => ([A[a], A[b]] = [A[b], A[a]]);

class Heap {
  constructor() {
    this.A = [0];
  }
  // 노드 C와 C의 부모 P를 뒤바꿔줌 => 끝에 하나를 삽입하고 쭉 끌어올릴 때 사용
  up(C) {
    const A = this.A;
    const P = Math.floor(C / 2);
    // 자식인 C의 우선 순위가 더 크면 종료
    if (C < 2 || A[C][1] > A[P][1]) return;
    swap(A, P, C);
    // 연쇄적으로 P도 up을 시켜줌
    this.up(P);
  }
  // 우선 순위가 가장 높은 하나를 뽑은 뒤에 남은 것들을 쭉 끌어내리는 데에 사용
  down(P) {
    const A = this.A;
    if (2 * P > A.length - 1) return;
    let C = 2 * P;
    if (2 * P + 1 < A.length && A[2 * P + 1][1] < A[2 * P][1]) C = 2 * P + 1;
    if (C > A.length - 1 || A[C][1] > A[P][1]) return;
    swap(A, P, C);
    this.down(C);
  }

  // 배열의 가장 마지막에 삽입 요소를 넣고 bubble up 시켜주는 함순
  mk(x) {
    const A = this.A;
    A.push(x);
    this.up(A.length - 1);
  }

  //
  rm() {
    const A = this.A;
    if (A.length < 2) return 0;
    const end = A.pop();
    if (A.length == 1) return end;
    // 제일 뒤에서 뽑아온 것을 제일 앞에 넣어주고 해당 배열을 반환
    const [min] = A.splice(1, 1, end);
    this.down(1);
    return min;
  }
}
const [V, E] = I[0].split(' ').map(Number);
// K는 시작점
const K = +I[1];
const G = Array.from({ length: V + 1 }, (_) => []);
for (let i = 2; i < E + 2; i++) {
  const [u, v, w] = I[i].split(' ').map(Number);
  G[u].push([v, w]);
}
const O = new Array(V + 1).fill('INF');
O[K] = 0;
const H = new Heap();
H.mk([K, 0]);
while (H.A.length > 1) {
  const [c, l] = H.rm();
  if (l > O[c]) continue;
  for (const [v, w] of G[c])
    if (l + w < O[v] || O[v] == 'INF') {
      O[v] = l + w;
      H.mk([v, O[v]]);
    }
}
O.shift();
console.log(O.join('\n'));
