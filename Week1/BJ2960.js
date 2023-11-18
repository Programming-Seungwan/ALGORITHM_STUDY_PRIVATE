// 백준 2960 에라토스테네스의 체 알고리즘
// https://www.acmicpc.net/problem/2960

const [n, k] = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split(' ')
  .map((v) => +v);

const arr = [];

for (let i = 2; i <= n; i++) arr.push(i);

let count = 0;
let prime;
let nth;

while (count < k) {
  prime = arr[0];
  // some 메서드를 사용하면 count가 K와 일치하는 가장 첫 번째 경우에 순회를 중지하고 빠져나갈 수 있다
  arr.some((v) => {
    if (v % prime === 0) {
      arr.splice(arr.indexOf(v), 1);
      nth = v;
      count++;
    }
    if (count === k) return true;
  });
}
console.log(nth);
