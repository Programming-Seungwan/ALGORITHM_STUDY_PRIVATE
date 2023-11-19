// 백준 파도반 수열 문제 #9461
// https://www.acmicpc.net/problem/9461

const fs = require('fs');
const [n, ...arr] = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map((v) => +v);

const MAX = Math.max(...arr);

let dp = [];
dp[0] = 1;
dp[1] = 1;
dp[2] = 1;

for (let i = 3; i <= MAX + 1; i++) {
  dp[i] = dp[i - 3] + dp[i - 2];
}

arr.forEach((v) => {
  console.log(dp[v - 1]);
});
