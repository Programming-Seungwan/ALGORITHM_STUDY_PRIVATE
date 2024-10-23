// 1. 특정 사용자가 들어옴 -> 이미 있는 사람이면 해당 UID를 찾아서 바꿔주고 새로 기록을 더해줌
// 2. 특정 사용자가 나감 -> 나갔다는 기록을 더해줌
// 3. 특정 사용자가 톡방 내에서 change함 -> 해당 UID를 찾아서 기록을 바꿔줌

// 사용자목록 -> 배열로 처리, 최신화할 기록 -> 배열로 처리(요소 : 닉네임, 입출력 여부, uid)

function solution(record) {
  const userList = []; // 실제 uid를 넣어놓을 배열
  const chattingRoomRecord = []; // 입출력 내역을 담아놓을 배열
  for (const recordElement of record) {
    const [newAction, newUidString, newNickName] = recordElement.split(' ');
    if (userList.indexOf(newUidString) === -1) {
      userList.push(newUidString);
      chattingRoomRecord.push({
        action: newAction,
        uidString: newUidString,
        nickname: newNickName,
      });
    } else {
      if (newAction === 'Enter') {
        chattingRoomRecord.forEach((el) => {
          if (el.uidString === newUidString) {
            el.nickname = newNickName
          }
        })
      }

      if (newAction === 'Leave') {}

      if (newAction === 'Change')
    }
  }

  return chattingRoomRecord;
}

console.log(
  solution([
    'Enter uid1234 Muzi',
    'Enter uid4567 Prodo',
    'Leave uid1234',
    'Enter uid1234 Prodo',
    'Change uid4567 Ryan',
  ])
);
