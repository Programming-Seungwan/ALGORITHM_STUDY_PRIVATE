// 레슨의 순서가 바뀌면 안됨 -> 끊는 블록이 필요함
// 블루레이 안에는 n개의 레슨이 들어가고 블루레이 자체는 M 개가 존재함
// 최대한 고르게 유지해야함
// 시작점, 끝점을 잡아야하는데, 이는 각각 가장 큰 요소와 전체 요소의 합이 된다.
//왼쪽이 오른쪽보다 작은 경우를 while의 조건으로 넣어준다
const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let [[N, M], lectures] = fs
  .readFileSync(filePath)
  .toString()
  .split('\n')
  .map((el) => el.split(' ').map((e) => +e));

let left = Math.max(...lectures);
let right = lectures.reduce((prev, curr) => prev + curr, 0);

while (left <= right) {
  const mid = Math.floor((left + right) / 2);
  // mid를 기준으로 잡았을 때의 블루레이 개수를 구해야 한다
  let sum = 0;
  let count = 0; // 갱신할 sum과 블루레이 개수를 나타낼 count 변수를 설정
  for (let i = 0; i < N; i++) {
    if (sum + lectures[i] > mid) {
      sum = 0;
      count += 1;
    }
    sum += lectures[i];
  }

  if (sum !== 0) {
    count += 1;
  }

  if (count > M) {
    left = mid + 1;
  } else {
    right = mid - 1;
  }
}

console.log(left);
