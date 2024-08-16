const fs = require('fs')
const filePath = process.platform === 'linux' ? "/dev/stdin" : "./input.txt"
const [n, ...arr] = fs.readFileSync(filePath).toString().trim().split('\n');

function getCombination(m, n) {
  let numerator = 1; // 분자
  let denominator = 1; // 분모

  for (let i = 0; i < n; i++) {
    numerator *= (m - i)
  }

  for (let i = 1; i <= n; i++) {
    denominator *= i
  }

  return Math.round(numerator / denominator)

}

for (let i = 0; i < n; i++) {
  const [n, m] = arr[i].split(' ').map(Number)
  console.log(getCombination(m, n));
}