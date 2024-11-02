// 틀리면 이전 퍼즐을 풀고 와야함. 이전 퍼즐은 무조건 맞다고 가정.
// diff는 현재 퍼즐 난이도, level은 내 실력, time_cur는 현재 문제 소요 시간, time_prev는 이전 퍼즐 소요시간
// 각 값들이 주어지면 level에 따라서 총 소요 시간을 구하는 로직이 필요함.
// 숙련도가 낮을 수록, 퍼즐을 해결하는 데에 걸리는 시간은 많아진다.

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

function solution(diffs, times, limit) {
  let level = 1;
  while (true) {
    if (getTotalTimeByLevel(diffs, times, level) <= limit) {
      return level;
    }
    level += 1;
  }
}

console.log(solution([1, 5, 3], [2, 4, 7], 30));
console.log(solution([1, 4, 4, 2], [6, 3, 8, 2], 59));
console.log(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723));
console.log(
  solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012)
);
