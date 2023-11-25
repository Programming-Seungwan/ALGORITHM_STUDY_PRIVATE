const fs = require('fs');
const { start } = require('repl');
let [inputString, explodeString] = fs.readFileSync('./input.txt').toString().trim().split('\n');

function removeBombString(originalString, bombString) {
  const bombStringLength = bombString.length;
  const startIndex = originalString.indexOf(bombString);

  if (startIndex === -1) return originalString;
  else {
    const originalStringArray = originalString.split('');
    originalStringArray.splice(startIndex, bombStringLength);
    return originalStringArray.join('');
  }
}

function removeBombStringRecursive(originalString, bombString) {
  const bombStringLength = bombString.length;
  const startIndex = originalString.indexOf(bombString);

  if (startIndex === -1) return originalString;
  else {
    const newStringArray = originalString.split('');
    newStringArray.splice(startIndex, bombStringLength);
    return removeBombStringRecursive(newStringArray.join(''), bombString);
  }
}

// 스택을 사용하는 정답 함수
function explodeString(s, bomb) {
  const stack = [];

  for (let char of s) {
    stack.push(char); // 현재 문자를 스택에 추가

    // 현재 추가된 문자열이 폭발 문자열의 끝과 일치하는지 확인
    if (stack.length >= bomb.length && stack.slice(-bomb.length).join('') === bomb) {
      // 폭발 문자열과 일치하면 제거
      stack.splice(-bomb.length);
    }
  }

  const result = stack.join('');
  return result || 'FRULA'; // 결과가 비어있으면 "FRULA" 반환
}

// 재귀를 사용하지 않고 반복문을 통하는 방식
// while (true) {
//   const result = removeBombString(inputString, explodeString);

//   if (result === inputString) break;
//   else inputString = result;
// }

// if (inputString.length === 0) console.log('FRULA');
// else console.log(inputString);

const result = removeBombStringRecursive(inputString, explodeString);

console.log(result.length === 0 ? 'FRULA' : result);
