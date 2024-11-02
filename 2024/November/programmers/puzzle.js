// 특정 배열과 숙련도를 받아서 총 소요 시간을 구해주는 함수
function getTotalTimeByLevel(diffs, times, level) {
  let totalTime = times[0]; // 전체 시간에 해당
  for (let i = 1; i < diffs.length; i++) {
    if (diffs[i] > level) {
      // 실력이 모자란 경우 -> 이전 문제 + 현재 문제를 차이만큼 풀고 새로 풀기
      const tmpTime = (diffs[i] - level) * (times[i] + times[i - 1]) + times[i];
      totalTime += tmpTime;
    } else {
      // 실력이 맞는 경우 : 그냥 바로 더해주면 됨
      totalTime += times[i];
    }
  }

  return totalTime;
}

// 이분법의 로직을 사용해야 함.
// start, end 포인터가 사용되어야 함
function solution(diffs, times, limit) {
  let start = 1;
  let end = 10 ** 15;

  while (true) {
    const level = Math.floor((start + end) / 2);
    const currentCost = getTotalTimeByLevel(diffs, times, level);
    const currentNextCost = getTotalTimeByLevel(diffs, times, level + 1);
    if (currentCost <= limit && currentNextCost > limit) {
      return level;
    }

    if (currentCost <= limit) {
      start = level;
    } else {
      end = level;
    }
  }
}
