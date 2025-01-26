const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().split('\n')

const [m, n, k] = input[0].split(' ').map(Number)
const secret = input[1].split(' ').map(Number)
const user = input[2].split(' ').map(Number)
let res = 'normal'

for (let i = 0; i <= n - m; i++) {
    let isMatch = true
    for (let j = 0; j < m; j++) {
        if (user[i + j] !== secret[j]) {
            isMatch = false
            break
        }
    }
    if (isMatch) {
        res = 'secret'
        break
    }
}

console.log(res)