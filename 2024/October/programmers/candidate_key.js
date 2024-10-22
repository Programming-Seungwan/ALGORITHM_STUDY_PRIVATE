// 키의 구성 length가 가장 적고 말고는 관심사가 아니다.
// 해당 키가 관련 튜플들을 구분하는지는 어떻게 판단할 것인가?

function solution(relation) {
  const numCols = relation[0].length; // 컬럼의 개수 -> 얘네들은 후보 필드들임
  const numRows = relation.length; // 튜플 자체의 개수
  const candidateKeys = []; // 후보 키를 저장할 배열

  // 모든 컬럼의 조합을 비트마스크로 생성
  for (let bitmask = 1; bitmask < 1 << numCols; bitmask++) {
    const uniqueSet = new Set();

    // 비트마스크에 따라 컬럼을 선택하여 튜플 생성
    for (let row = 0; row < numRows; row++) {
      let tuple = '';
      for (let col = 0; col < numCols; col++) {
        if (bitmask & (1 << col)) {
          tuple += relation[row][col] + ',';
        }
      }
      uniqueSet.add(tuple); // 유일성 검사
    }

    // 유일성을 만족하는 경우
    if (uniqueSet.size === numRows) {
      // 최소성 검사
      let isMinimal = true;
      for (const key of candidateKeys) {
        if ((bitmask & key) === key) {
          isMinimal = false;
          break;
        }
      }

      // 최소성을 만족하면 후보 키에 추가
      if (isMinimal) {
        candidateKeys.push(bitmask);
      }
    }
  }

  // 후보 키의 개수를 반환
  return candidateKeys.length;
}
ㄴ;
