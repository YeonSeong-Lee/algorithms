const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().split('\n')

const [n, m] = input[0].split(' ').map(Number)
const real = []
const exp = []
for (let i = 0; i < n; i++) {
    const [cur, speed] = input[i + 1].split(' ').map(Number)
    for (let j = 0; j < cur; j++) {
        real.push(speed)
    }
}
for (let i = 0; i < m; i++) {
    const [cur, speed] = input[i + 1 + n].split(' ').map(Number)
    for (let j = 0; j < cur; j++) {
        exp.push(speed)
    }
}

let res = 0

for (let i = 0; i < real.length; i++) {
    res = Math.max(res, exp[i] - real[i])
}

console.log(res)