const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const data = fs.readFileSync(filePath).toString().split('\n');
const [num, sum] = data[0].split(' ').map((element) => +element);
const dataArray = data[1].split(' ').map((element) => +element);

// 시작과 종료 포인터를 만들어두기.
// 바깥의 조건문에서 항상 처음 시작과 마지막을 만들어준다.
let flag = false;

for (let i = 1; i <= num; i++) {
  let startPoint = 0;
  let endPoint = startPoint + i;
  while (endPoint <= num - 1) {
    const tmpPart = dataArray.slice(startPoint, endPoint + 1);
    const tmpPartSum = tmpPart.reduce((prev, curr) => prev + curr, 0);

    if (tmpPartSum >= sum) {
      flag = true;
      break;
    } else {
      startPoint += 1;
      endPoint += 1;
    }
  }

  if (flag === true) {
    console.log(endPoint - startPoint + 1);
    break;
  }
}
