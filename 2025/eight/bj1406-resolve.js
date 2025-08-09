const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';

const [firstString, N, ...commandArray] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split('\n');

const newCommandArray = commandArray.map((el) => el.split(' '));

// 커서를 하나 왼쪽으로로 옮기는 함수
const moveCursorLeft = (arr) => {
  const tmpArray = []; // 잠시 넣어놓을 배열
  while (true) {
    const poppedItem = arr.pop();
    if (poppedItem !== 'cursor') {
      tmpArray.push(poppedItem);
    } else {
      const tmpPoppedItem = arr.pop();
      tmpArray.push(tmpPoppedItem);
      arr.push('cursor');
      tmpArray.reverse();
      for (let i = 0; i < tmpArray.length; i++) {
        arr.push(tmpArray[i]);
      }
      break;
    }
  }
};

// 커서를 우측으로 옮기는 함수
const moveCursorRight = (arr) => {
  const tmpArray = [];

  while (true) {
    const poppedItem = arr.pop();
    if (poppedItem !== 'cursor') {
      tmpArray.push(poppedItem);
    } else {
      const tmpPoppedItem = tmpArray.pop();
      arr.push(tmpPoppedItem);
      arr.push('cursor');
      tmpArray.reverse();
      for (let i = 0; i < tmpArray.length; i++) {
        arr.push(tmpArray[i]);
      }
      break;
    }
  }
};

const removeLeft = (arr) => {
  const tmpArray = [];

  while (true) {
    const poppedItem = arr.pop();
    if (poppedItem !== 'cursor') {
      tmpArray.push(poppedItem);
    } else {
      arr.pop();
      arr.push('cursor');
      tmpArray.reverse();
      for (let i = 0; i < tmpArray.length; i++) {
        arr.push(tmpArray[i]);
      }
      break;
    }
  }
};

const insertDollar = (arr, char) => {
  const tmpArray = [];

  while (true) {
    const poppedItem = arr.pop();
    if (poppedItem !== 'cursor') {
      tmpArray.push(poppedItem);
    } else {
      arr.push(char);
      arr.push('cursor');
      tmpArray.reverse();
      for (let i = 0; i < tmpArray.length; i++) {
        arr.push(tmpArray[i]);
      }
      break;
    }
  }
};

// L D B P

const myArr = firstString.split('');
myArr.push('cursor');
for (const command of newCommandArray) {
  const commandChar = command[0];
  if (commandChar === 'L') {
    moveCursorLeft(myArr);
  } else if (commandChar === 'D') {
    moveCursorRight(myArr);
  } else if (commandChar === 'B') {
    removeLeft(myArr);
  } else if (commandChar === 'P') {
    const insertChar = command[1];
    insertDollar(myArr, insertChar);
  }
}

const resultArr = myArr.filter((item) => item !== 'cursor' && item);
console.log(resultArr.join(''));
