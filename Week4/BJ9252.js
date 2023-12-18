const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';

const [firstSequence, secondSequence] = fs.readFileSync(filePath).toString().trim().split('\n');

function longestCommonSubsequence(str1, str2) {
  const m = str1.length;
  const n = str2.length;
  const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(''));

  // 이 방식은 아래에서부터 쌓아 올라가는 방식을 택했다.
  // 동적 프로그래밍은 bottom - up과 top - down 중 어떤 것을 택할지 결정하는 것이 포인트!
  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (str1[i - 1] === str2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + str1[i - 1];
      } else {
        dp[i][j] = dp[i - 1][j].length > dp[i][j - 1].length ? dp[i - 1][j] : dp[i][j - 1];
      }
    }
  }

  return dp[m][n];
}

const result = longestCommonSubsequence(firstSequence, secondSequence);
const resultLength = result.length;

console.log(resultLength);
if (resultLength !== 0) console.log(result);
