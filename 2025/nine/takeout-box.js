const makeBoxArray = (totalNum, width) => {
  let totalNumVar = totalNum;
  const result = [];
  let flag = true; // 정방향일떄 true, 역방향일때는 false
  let startIndex = 1; // 기록할 숫자 변수
  while (true) {
    const tmpLeftCount = totalNumVar - width;
    if (tmpLeftCount <= 0) {
      // 이 턴까지만 하고 끝내기
      const lastElementLength = totalNum - startIndex + 1;
      const pushingArray = [];
      for (let i = startIndex; i < startIndex + lastElementLength; i++) {
        pushingArray.push(i);
      }
      const lackCount = width - pushingArray.length;

      if (flag) {
        for (let i = 0; i < lackCount; i++) {
          pushingArray.push(null);
        }

        result.unshift(pushingArray);
      } else {
        for (let i = 0; i < lackCount; i++) {
          pushingArray.push(null);
        }
        result.unshift(pushingArray.reverse());
      }
      break;
    } else {
      // 밀어넣고 flag랑 totalNumber 바꿔야지
      const pushingArray = [];
      for (let i = startIndex; i < startIndex + width; i++) {
        pushingArray.push(i);
      }
      if (flag) {
        result.unshift(pushingArray);
      } else {
        result.unshift(pushingArray.reverse());
      }

      flag = !flag;
      totalNumVar -= width;
      startIndex += width;
    }
  }

  return result;
};

function solution(n, w, num) {
  const boxArray = makeBoxArray(n, w);
  for (let i = 0; i < boxArray.length; i++) {
    for (let j = 0; j < w; j++) {
      if (boxArray[i][j] === num) {
        return boxArray[0][j] === null ? i : i + 1;
      }
    }
  }
}
