import sys

input = sys.stdin.readline


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clock or counterclockwise


def onSegment(p, q, r):
    return (
        q[0] <= max(p[0], r[0])
        and q[0] >= min(p[0], r[0])
        and q[1] <= max(p[1], r[1])
        and q[1] >= min(p[1], r[1])
    )


def doIntersect(p1, q1, p2, q2):
    # Find orientations
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # Special Cases
    if o1 == 0 and onSegment(p1, p2, q1):
        return True
    if o2 == 0 and onSegment(p1, q2, q1):
        return True
    if o3 == 0 and onSegment(p2, p1, q2):
        return True
    if o4 == 0 and onSegment(p2, q1, q2):
        return True

    return False


# Input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# Check if the line segments intersect
if doIntersect((x1, y1), (x2, y2), (x3, y3), (x4, y4)):
    print(1)
else:
    print(0)
