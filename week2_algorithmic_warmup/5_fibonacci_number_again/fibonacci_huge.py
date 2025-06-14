def fibonacci_huge_naive(n, m):
    fib_list = [0, 1]
    if n <= 1:
        return n
    i = 2
    while True:
        prev = fib_list[i - 1]
        prev_prev = fib_list[i - 2]
        current = (prev + prev_prev) % m
        if current == 0 and prev == 1:
            break
        fib_list.append(current)
        i += 1

    freq = len(fib_list)
    rem = n % freq
    return fib_list[rem]


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
