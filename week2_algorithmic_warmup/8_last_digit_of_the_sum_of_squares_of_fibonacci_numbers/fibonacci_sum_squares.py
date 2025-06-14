def fibonacci_sum_squares(n):
    freq = 60
    fib_list = [0, 1]
    fib_sq_list = [0, 1]

    for i in range(2, freq):
        last = (fib_list[i - 1] + fib_list[i - 2]) % 10
        fib_list.append(last)
    fib_sq_list = list(map(lambda x: (x**2) % 10, fib_list))

    rem = n % freq
    return sum(fib_sq_list[0 : rem + 1]) % 10


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_sum_squares(n))
