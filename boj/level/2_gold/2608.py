import sys

input = sys.stdin.readline

roam_arab_one_pices = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
roam_arab_two_pices = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
roam_arab = {**roam_arab_one_pices, **roam_arab_two_pices}
roam_arab = dict(sorted(roam_arab.items(), key=lambda x: x[1], reverse=True))
arab_roam = {value: key for key, value in roam_arab.items()}


def convert_roam_to_arab(str):
    ret = 0
    i = 0
    while i < len(str):
        if str[i : i + 2] in roam_arab_two_pices:
            ret += roam_arab_two_pices[str[i : i + 2]]
            i += 2
        elif str[i] in roam_arab_one_pices:
            ret += roam_arab_one_pices[str[i]]
            i += 1
        else:
            i += 1
    return ret


def convert_arab_to_roam(num):
    temp = []
    for e in arab_roam:
        if num // e > 0:
            temp.append(arab_roam[e] * (num // e))
            num -= e * (num // e)

    return "".join(temp)


a = input()
b = input()
sum_a_b = convert_roam_to_arab(a) + convert_roam_to_arab(b)
print(sum_a_b)
print(convert_arab_to_roam(sum_a_b))
