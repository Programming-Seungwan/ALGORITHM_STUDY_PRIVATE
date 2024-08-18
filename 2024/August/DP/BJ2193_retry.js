const fs = require('fs')
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const number = Number(fs.readFileSync(filePath).toString().trim())

// dp[n] = 2* dp[n - 1][0] + dp[n - 1][1] -> 2차원 리스트로 풀 수 있는 점화식에 해당함

const dp = []
for (let i = 0; i<= number; i++) {
  dp.push([0, 0])
}

dp[1][1] = 1;
if (number >=2) {
  dp[2][0] = 1;
}


if (number >= 3) {
  for (let i = 3; i <= number; i++) {
    dp[i][0] = BigInt(dp[i - 1][0]) + BigInt(dp[i - 1][1]);
    dp[i][1] = BigInt(dp[i - 1][0]);
  }
}

console.log(BigInt(dp[number][0] + dp[number][1]).toString());