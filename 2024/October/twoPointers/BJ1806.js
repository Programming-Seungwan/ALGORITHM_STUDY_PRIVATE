const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';

// 해당 문제를 왜 투 포인터로 풀어야 하는가? 어찌보면 그냥 브루트 포스 알고리즘 아닌가?
// 투 포인터와 정렬은 의미가 있을까? ㄴㄴ 이미 투 포인터를 쓴다는 것부터가 위계질서를 요소 간에 세우지 않는다는 것이다.
const data = fs.readFileSync(filePath).toString().split('\n');
const [num, sum] = data[0].split(' ').map((element) => +element);
const dataArray = data[1].split(' ').map((element) => +element);
let flag = false;

for (let i = 1; i <= num; i++) {
  let startIndex = 0;
  let endIndex = startIndex + i;
  while (endIndex <= dataArray.length - 1) {
    const tmpSum = dataArray
      .slice(startIndex, endIndex + 1)
      .reduce((prev, curr) => prev + curr, 0);

    if (tmpSum === sum) {
      console.log(i + 1);
      flag = true;
      break;
    } else {
      startIndex += 1;
      endIndex += 1;
    }
  }

  if (flag) break;
}
