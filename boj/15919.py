# 15919 사자는 여행왕이야


import sys

input = sys.stdin.readline


def isOverlap(a, b):

    START, END = 0, 1

    if (a[START] <= b[START] and a[END] >= b[END]):
        return True

    elif (a[START] >= b[START] and a[END] <= b[END]):
        return True

    elif (a[START] <= b[START] and a[END] >= b[START]):
        return True

    elif (a[START] <= b[END] and a[END] >= b[END]):
        return True

    else:

        return False


def isPossiblePath(travel_candiate_index, visited):

    for i in range(len(travel_candiates)):

        if not isOverlap(travel_candiates[travel_candiate_index], travel_candiates[i]):
            return True

    return False


def getLogestCommonDay(travel_candiates, visited):

    for i in range(len(travel_candiates)):

        if (visited[travel_candiates[i][0]] == False and visited[travel_candiates[i][1]] == False):

            visited[travel_candiates[i][0]] = True

            visited[travel_candiates[i][1]] = True

            return 1 + getLogestCommonDay(travel_candiates, visited)


N = int(input())

M = int(input())
travel_candiates = []

visited = [False] * N


for _ in range(M):

    travel_candiates.append(dq(map(int, (input().split()))))
