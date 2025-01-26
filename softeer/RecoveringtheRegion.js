const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().split('\n')
const dirs = [[0,1], [1 , 0], [-1,0], [0, -1]]
const res = []

let [n, ...arr] = input
n = +n
const visited = Array(n*n).fill(false)
arr = arr.map(l => l.split('').map(v => +v))

function bfs(y, x) {
    cnt = 0
    if (visited[y*n + x] == true) {
        return
    }
    const q = [[y,x]]
    visited[n * y + x] = true
    while (q.length > 0) {
        const [cy, cx] = q.shift()

        if (arr[cy][cx] == 1) {
            cnt += 1
        }
        for (const [dy, dx] of dirs) {
            const ny = cy + dy
            const nx = cx + dx

            if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
                continue
            }
            if (visited[ny * n + nx]) {
                continue
            }
            q.push([ny,nx])
            visited[ny * n + nx] = true
        }
    }
    if (cnt != 0) {
        res.push(cnt) 
    }
}


for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
        bfs(i, j)
    }
}

console.log(res)