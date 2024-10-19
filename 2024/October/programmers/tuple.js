// 튜플은 중복된 원소를 가질 수 있으며, 순서가 다른 튜플은 서로 다른 것임
// 각 집단을 쪼개서 배열로 저장하고, js의 set에 넣는 연산 과정을 거치자.
// 자료형으로 정리할 수 있느 능력이 필요함.
// {가 시작되었을 때에는 그냥 넘기고 , 일떄는 그냥 넘겨야 됨

function makeInputStringRefined(s) {
  if (s.indexOf(',') === -1) {
    const tmpData = [[...s].splice(2, s.length - 4)];
    return [[+tmpData[0].join('')]];
  }

  const tmpS = [...s].splice(2, s.length - 4);

  return tmpS
    .join('')
    .split('},{')
    .map((el) => el.split(',').map((tmpEl) => +tmpEl));
}

function solution(s) {
  const refinedArray = makeInputStringRefined(s);
  const resultArray = []; // 결과로 반환할 배열에 해당함
  const resultSet = new Set();

  refinedArray.sort((first, second) => first.length - second.length);
  for (const refinedArrayElement of refinedArray) {
    for (const refinedArrayInnerElement of refinedArrayElement) {
      if (!resultSet.has(refinedArrayInnerElement)) {
        resultSet.add(refinedArrayInnerElement);
        resultArray.push(refinedArrayInnerElement);
      }
    }
  }

  return resultArray;
}

solution('{{2},{2,1},{2,1,3},{2,1,3,4}}');
solution('{{1,2,3},{2,1},{1,2,4,3},{2}}');
solution('{{20,111},{111}}');
solution('{{123}}');
solution('{{4,2,3},{3},{2,3,4,1},{2,3}}');
