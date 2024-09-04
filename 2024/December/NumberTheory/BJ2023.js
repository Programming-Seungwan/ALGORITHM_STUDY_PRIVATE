const fs = require('fs');
const filepath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const num = Number(fs.readFileSync(filepath).toString().trim());
const memoObject = {};
for (let i = 1; i <= num; i++) {
  memoObject[i] = [];
}

memoObject[1] = [2, 3, 5, 7];

// 소수인지를 판별하는 함수를 작성
// 기존의 숫자가 소수이면, 하나를 더 붙였을 경우만 판단하면 계산 리소스를 줄일 수 있음
// 소수를 판단하는 법
// 1. 2와 3 거르기 2. 짝수 거르기 3. 3부터 자기 자신의 제곱근까지 돌려서 나누어 떨어지는지를 확인.

function isPrime(num) {
  // 1은 소수가 아니므로 false 반환
  if (num <= 1) return false;

  // 2와 3은 소수이므로 true 반환
  if (num === 2 || num === 3) return true;

  // 짝수는 소수가 아니므로 false 반환
  if (num % 2 === 0) return false;

  // num이 2 또는 3으로 나누어지지 않는 경우
  // 소수 여부 판단을 위해 √num까지만 나눠서 확인
  for (let i = 3; i <= Math.sqrt(num); i += 2) {
    if (num % i === 0) {
      return false;
    }
  }

  return true;
}

for (let i = 2; i <= num; i++) {
  for (const beforeNum of memoObject[i - 1]) {
    for (let j = 0; j <= 9; j++) {
      const newNumber = Number(String(beforeNum).concat(String(j)));
      if (isPrime(newNumber)) {
        memoObject[i].push(newNumber);
      }
    }
  }
}

for (const printNumber of memoObject[num]) {
  console.log(printNumber);
}
