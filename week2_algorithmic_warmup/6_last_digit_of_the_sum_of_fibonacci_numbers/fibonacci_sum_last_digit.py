def fibonacci_sum(n):
    fib_list = [0, 1]
    for i in range(2, n + 1):
        prev = fib_list[i - 1] % 10
        prev_prev = fib_list[i - 2] % 10
        curr = (prev + prev_prev) % 10
        if curr == 0 and prev == 1:
            break
        fib_list.append(curr)

    freq = len(fib_list)
    sum_freq = ((sum(fib_list) % 10) * (n // freq)) % 10
    sum_rest = sum(fib_list[0 : n % freq + 1]) % 10

    return (sum_freq + sum_rest) % 10


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_sum(n))
