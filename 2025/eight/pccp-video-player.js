// 시간을 숫자로 계산해주는 함수
function turnTimeStringToNumber(timeString) {
  const [hour, minute] = timeString.split(':').map((time) => parseInt(time));

  return 60 * hour + minute;
}

// 움직이고 위치를 결정할 함수
function determineFinalPos(posNum, opStartNum, opEndNum) {
  if (posNum >= opStartNum && posNum <= opEndNum) {
    return opEndNum;
  } else {
    return posNum;
  }
}

function executeCommand(videoLenNum, posNum, opStartNum, opEndNUm, command) {
  let tmpReturnNum = 0;
  if (command === 'next') {
    const tmpNextPos = posNum + 10;
    if (tmpNextPos > videoLenNum) {
      tmpReturnNum = videoLenNum;
    } else {
      tmpReturnNum = tmpNextPos;
    }
  } else if (command === 'prev') {
    const tmpNextPos = posNum - 10;
    if (tmpNextPos < 0) {
      tmpReturnNum = 0;
    } else {
      tmpReturnNum = tmpNextPos;
    }
  }

  return determineFinalPos(tmpReturnNum, opStartNum, opEndNUm);
}

function solution(video_len, pos, op_start, op_end, commands) {
  const videoLenNum = turnTimeStringToNumber(video_len);
  let posNum = turnTimeStringToNumber(pos);
  const opStartNum = turnTimeStringToNumber(op_start);
  const opEndNum = turnTimeStringToNumber(op_end);

  for (command of commands) {
    posNum = determineFinalPos(posNum, opStartNum, opEndNum);
    posNum = executeCommand(videoLenNum, posNum, opStartNum, opEndNum, command);
  }

  const hour = Math.floor(posNum / 60)
    .toString()
    .padStart(2, '0');
  const minute = (posNum % 60).toString().padStart(2, '0');

  return `${hour}:${minute}`;
}
