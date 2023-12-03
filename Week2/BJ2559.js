// 백준 2559 수열 문제
// https://www.acmicpc.net/problem/2559
// 아래 문제는 투 포인터 슬라이딩 윈도우 기법으로 만든 풀이
const fs = require('fs');
const [first, second] = fs.readFileSync('./input.txt').toString().trim().split('\n');

// 총 data의 길이는 inputNum이고 연속된 길이는 size이다.
const [inputNum, size] = first.split(' ').map((member) => +member);

// 입력값으로 주어지는 배열이다. 이것을 순회하면 됨
const dataArray = second.split(' ').map((member) => +member);

let startIndex = 0;
let endIndex = startIndex + size - 1;

let answer = 0;

// 정답 값을 초기화 한다.
for (let i = startIndex; i <= endIndex; i++) {
  answer += dataArray[i];
}

let prevArraySum = answer;

startIndex++;
endIndex++;

while (startIndex <= inputNum - size) {
  prevArraySum = prevArraySum - dataArray[startIndex - 1] + dataArray[endIndex];

  if (prevArraySum > answer) {
    answer = prevArraySum;
  }

  startIndex++;
  endIndex++;
}

console.log(answer);
