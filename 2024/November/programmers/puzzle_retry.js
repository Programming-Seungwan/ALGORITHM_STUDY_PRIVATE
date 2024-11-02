function solution(diffs, times, limit) {
  let max = 100000,
    min = 1,
    mid = undefined;
  let answer = max;
  while (min <= max) {
    mid = Math.floor((max + min) / 2);
    let spendTime = 0,
      over = false;
    // 끝까지 돌았는데, 제한 시간을 넘어 갔는지를 의미. 넘어갔으면 over라고 하고 하방을 높여주기
    for (let i = 0; i < diffs.length; ++i) {
      if (mid - diffs[i] < 0) {
        spendTime =
          spendTime + (diffs[i] - mid) * (times[i] + times[i - 1]) + times[i];
      } else {
        spendTime += times[i];
      }

      if (limit < spendTime) {
        over = true;
        break;
      }
    }

    if (over) {
      min = mid + 1;
    } else {
      answer = mid;
      max = mid - 1;
    }
  }
  return answer;
}
