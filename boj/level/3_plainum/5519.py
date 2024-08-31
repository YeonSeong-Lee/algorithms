from itertools import permutations


is_prime = [True] * 100000


def generate_primes():
    primes = []
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(100000 ** 0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, 100000, num):
                is_prime[multiple] = False

    for num in range(10000, 100000):
        if is_prime[num]:
            primes.append(num)

    return primes


def is_prime_f(n):
    return is_prime[n]


def digit_sum(n):
    return sum(int(digit) for digit in str(n))


def find_magic_squares(digit_sum_value, top_left_value):
    primes = generate_primes()
    valid_primes = [p for p in primes if digit_sum(p) == digit_sum_value]
    results = []

    def is_valid_squqre():

    for perm in permutations(valid_primes, 24):
        square = [[top_left_value] + list(perm[:4])]
        for i in range(1, 5):
            square.append(list(perm[4*(i-1)+4:4*i+4]))
        if is_valid_square(square):
            results.append(square)

    return results


def main():
    digit_sum_value = int(input())
    top_left_value = int(input())

    results = find_magic_squares(digit_sum_value, top_left_value)

    for result in results:
        for row in result:
            print(''.join(map(str, row)))
        print()


if __name__ == "__main__":
    main()
