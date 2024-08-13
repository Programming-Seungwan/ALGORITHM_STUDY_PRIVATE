const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [n, ...arr] = fs.readFileSync(filePath).toString().trim().split('\n')
const memoArray = arr.map((memoStr) => memoStr.split(' '))

const logDictionary = {}
for (const logElement of memoArray) {
  const personName = logElement[0];
  const personState = logElement[1];

  if (logDictionary[personName] === undefined) {
    logDictionary[personName] = 1;
  } else {
    if (personState === 'enter') {
      logDictionary[personName] = 1;
    } else if (personState === 'leave') {
      logDictionary[personName] = 0;
    }
  }
}

const logArray = [];
for (const lg in logDictionary) {
  if (logDictionary[lg] === 1) {
    logArray.push(lg)
  }
}

console.log(logArray.sort().reverse().join('\n'))