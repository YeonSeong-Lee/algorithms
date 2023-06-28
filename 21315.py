# 21315 카드 섞기

N = int(input())
init_cards = list(range(1, N+1))
cards = list(map(int, input().split()))


def suffle(k, cards):
    if k == 1:
        return cards
    else:
        cards = cards[:2 ** k - 1] + suffle(k-1, cards[2 ** k - 1:])


print(suffle(2, init_cards))
