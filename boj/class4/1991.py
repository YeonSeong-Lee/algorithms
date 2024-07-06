import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
graph = [['.', '.'] for _ in range(n)]
for _ in range(n):
  s, l, r = input().split()
  graph[ord(s) - ord('A')][0] = l
  graph[ord(s) - ord('A')][1] = r

def preorder(cur):
  print(cur, end='')
  left, right = graph[ord(cur)-ord('A')]
  if left != '.':
    preorder(left)
  if right != '.':
    preorder(right)

def inorder(cur):
  left, right = graph[ord(cur)-ord('A')]
  if left != '.':
    inorder(left)
  print(cur, end='')
  if right != '.':
    inorder(right)

def postorder(cur):
  left, right = graph[ord(cur)-ord('A')]
  if left != '.':
    postorder(left)
  if right != '.':
    postorder(right) 
  print(cur, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
  

