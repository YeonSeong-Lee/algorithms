const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [N, K] = input[0].split(' ').map(x => parseInt(x));

const arrByNameLength = Array(19).fill(0).map(x => []);
let totalBestFriend = 0;


for (let i = 1; i <= N; i++) {
    arrByNameLength[input[i].length - 2].push(i);
}

for (let i = 0; i < arrByNameLength.length; i++) {
    if (arrByNameLength[i].length === 0 || arrByNameLength[i].length === 1 ) {
        continue;
    }
    for (let j = 0; j < arrByNameLength[i].length; j++) {
        for (let k = arrByNameLength[i].length - 1; k > j; k--) {
            if (arrByNameLength[i][k] - arrByNameLength[i][j] <= K) {
                totalBestFriend += k - j;
                break;
            }
        }
    }
}

console.log(totalBestFriend);
