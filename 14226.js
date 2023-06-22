const fs = require('fs');
const goal = fs.readFileSync('ex01').toString().split('\n').map(x => parseInt(x, 10))[0];
// const goal = fs.readFileSync('/dev/stdin').toString().split('\n').map(x => parseInt(x, 10))[0];

const initInfo = { screen: 1, clip: 0, time: 0 };
const MAX_SIZE = 1000;
const queue = [initInfo];
const visted = Array(MAX_SIZE + 1).fill(0).map(x => Array(MAX_SIZE + 1).fill(false));
visted[1][0] = true;

while (queue.length > 0) {
    const { screen, clip, time } = queue.shift();
    if (screen === goal) {
        console.log(time);
        break;
    }
    // 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
    if (screen != clip && !visted[screen][screen]) {
        queue.push({ screen: screen, clip: screen, time: time + 1 });
        visted[screen][screen] = true;
    }
    // 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
    if (clip > 0 && screen + clip <= MAX_SIZE && !visted[screen + clip][clip]) {
        queue.push({ screen: screen + clip, clip: clip, time: time + 1 });
        visted[screen + clip][clip] = true;
    }
    // 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
    if (screen > 0 && !visted[screen - 1][clip]) {
        queue.push({ screen: screen - 1, clip: clip, time: time + 1 });
        visted[screen - 1][clip] = true;
    }
}
