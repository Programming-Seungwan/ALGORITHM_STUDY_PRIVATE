const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';

const [firstString, N, ...commandArray] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split('\n');

function swapAdjacent(arr, index) {
  if (index < 0 || index >= arr.length - 1) return;
  [arr[index], arr[index + 1]] = [arr[index + 1], arr[index]];
}

const stack = firstString.split('');
stack.push('cursor');
let cursorIndex = stack.length - 1;

const newCommandArray = commandArray.map((el) => el.split(' '));

for (let newCommandElement of newCommandArray) {
  const command = newCommandElement[0];
  if (command === 'L' && cursorIndex !== 0) {
    swapAdjacent(stack, cursorIndex - 1);
    cursorIndex--;
  } else if (command == 'D') {
    swapAdjacent(stack, cursorIndex);
    cursorIndex++;
  } else if (command === 'B') {
    if (cursorIndex !== 0) {
      stack.splice(cursorIndex - 1, 1);
      cursorIndex--;
    }
  } else if (command === 'P') {
    const newChar = newCommandElement[1];
    stack.splice(cursorIndex, 0, newChar);
    cursorIndex++;
  }
}

console.log(stack.filter((el) => el !== 'cursor').join(''));
