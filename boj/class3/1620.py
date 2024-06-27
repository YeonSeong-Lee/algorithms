import sys
input = sys.stdin.readline

numbers = {}
pokemon = {}


n, m = map(int, input().split())
for i in range(1, n + 1):
    temp = input().strip()
    numbers[i] = temp
    pokemon[temp] = i


for _ in range(m):
    problem = input().strip()
    if problem.isdigit():
        print(numbers[int(problem)])
    else:
        print(pokemon[problem])16
    
