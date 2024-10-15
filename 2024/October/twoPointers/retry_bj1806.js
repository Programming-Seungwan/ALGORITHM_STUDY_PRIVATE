const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const inputData = fs.readFileSync(filePath).toString().split('\n');

const [n, s] = inputData[0].split(' ').map((el) => +el);
const dataArray = inputData[1].split(' ').map((el) => +el);
// 왼포인터와 오른쪽 포인터는 둘다 0으로부터 시작한다
// 사실 그냥 전체를 싹 흝으면서 점검하면 되는데, 이걸 어떻게 효율적으로 할지에 관한 문제이다
// 오른쪽 포인터를 늘려가는 식으로 진행하는데, 왼쪽 포인터가 끝을 안넘어가면 된다.
// 부분합이 작으면 오른쪽 포인터를 늘려서 부분합을 확장하고, 부분합이 크거나 같으면 왼 포인터를 늘린다.
let leftPointer = 0;
let rightPointer = 0;
let sum = 0;

let minLength = Infinity;

while (rightPointer < n) {
  sum += dataArray[rightPointer];

  while (sum >= s) {
    // 해당 while 절에서는 right가 고정된 상태에서 가장 짧은 만족하는 부분합을 만들어야 함
    minLength = Math.min(minLength, rightPointer - leftPointer + 1);
    sum -= dataArray[leftPointer];
    leftPointer += 1;
  }

  rightPointer += 1;
}

console.log(minLength === Infinity ? 0 : minLength);
