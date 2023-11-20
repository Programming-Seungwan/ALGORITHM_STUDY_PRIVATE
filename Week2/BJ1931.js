// 백준 1931번 회의실 배정 문제
// https://www.acmicpc.net/problem/1931
const fs = require('fs');
const [n, ...arr] = fs.readFileSync('./input.txt').toString().trim().split('\n');

const scheduleArray = [];

for (let i = 0; i < arr.length; i++) {
  const schedule = arr[i].split(' ');
  schedule[0] = parseInt(schedule[0]);
  schedule[1] = parseInt(schedule[1]);

  scheduleArray.push(schedule);
}
let meetingCount = 0;
let endingTime = 0;

// 해당 문제 풀이로 풀면 중첩된 for문으로 인해서 시간 초과 문제가 발생할 수 있다 => 미리 sort()를 통해 일정 배열을 정렬한다
// while (scheduleArray.some((v) => v[0] >= endingTime)) {
//   시작 시간이 endingTime보다 이후인 첫번쨰 요소를 찾기
//   let someSchedule = scheduleArray.find((v) => endingTime <= v[0]);

//   for (let i = 0; i < scheduleArray.length; i++) {
//     if (scheduleArray[i][0] >= endingTime && scheduleArray[i][1] <= someSchedule[1]) someSchedule = scheduleArray[i];
//   }

//   endingTime = someSchedule[1];
//   meetingCount++;
// }

// scheduleArray를 정렬해줄 필요가 있음
// sort는 오름차순을 디폴트로 생각하기 때문에 return 값이 양수면 b를 a보다 앞으로 위치시킨다

scheduleArray.sort((a, b) => {
  // 종료 시간이 빠른 것을 우선적으로 앞으로 보내고, 같다면 시작 시간이 빠른 것을 앞으로 보낸다
  if (a[1] === b[1]) {
    return a[0] - b[0];
  } else {
    return a[1] - b[1];
  }
});

scheduleArray.forEach((schedule) => {
  if (endingTime <= schedule[0]) {
    meetingCount++;
    endingTime = schedule[1];
  }
});

console.log(meetingCount);
