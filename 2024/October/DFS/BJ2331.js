// dfs는 스택 자료 구조를 이용하는데, 스택에 넣고 빼나가며 주변 노드들이 모두 visited 되었으면 해당 함수를 종료하는 알고리즘임
// nodeJS에서는 dfs의 visited를 set() 자료형으로 묶고 추가하면 has() 등의 메서드를 이용하는 것은 어떤가
const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';

const [A, P] = fs
  .readFileSync(filePath)
  .toString()
  .split(' ')
  .map((element) => parseInt(element));

function getGopNewNumber(originalNumber, time) {
  let result = 0;
  const stringOriginalNumber = originalNumber.toString();

  for (let i = 0; i < stringOriginalNumber.length; i++) {
    result += stringOriginalNumber[i] ** time;
  }

  return result;
}

const visited = new Set();

let nextNumber = A;
visited.add(nextNumber);

while (true) {
  const newCalculatedNumber = getGopNewNumber(nextNumber, P);
  if (!visited.has(newCalculatedNumber)) {
    visited.add(newCalculatedNumber);
    nextNumber = newCalculatedNumber;
  } else {
    // 이미 들어간 경우. 거기서부터 타고 들어가서 다 빼야됨
    let nowNumber = newCalculatedNumber;
    let nextNumber = getGopNewNumber(newCalculatedNumber, P);

    while (visited.has(nowNumber)) {
      visited.delete(nowNumber);
      nowNumber = nextNumber;
      nextNumber = getGopNewNumber(nextNumber, P);
    }
    break;
  }
}

console.log([...visited.keys()].length);

// 핵심 포인트? 특정 숫자가 기존의 자료구조에 있는지를 구하기. 근데 set으로 하면 그 다음거를 다 지워버려야됨
// 특정 노드부터 끝까지 타고 들어가서 다 제거해버리면 됨
