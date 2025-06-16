# Uses python3
import sys


def fibonacci_partial_sum_naive(m, n):
    fib_list = [0, 1]
    for i in range(2, n + 1):
        prev = fib_list[i - 1] % 10
        prev_prev = fib_list[i - 2] % 10
        curr = (prev + prev_prev) % 10
        if curr == 0 and prev == 1:
            break
        fib_list.append(curr)

    freq = len(fib_list)

    x = m % freq
    y = n % freq
    sumz = 0

    if x > y:
        sumz = sum(fib_list[x:]) + sum(fib_list[0 : y + 1])
    else:
        sumz = sum(fib_list[x : y + 1])
    return sumz % 10


if __name__ == "__main__":
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
