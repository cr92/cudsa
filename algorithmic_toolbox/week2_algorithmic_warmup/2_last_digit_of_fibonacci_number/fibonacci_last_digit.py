# The last digit of Fib(N) depends only the last digits on and Fib(N-1) and Fib(N-2)
# Way 1: Find the Nth Fibonacci number and its %10. Can overflow if N is big.
# Way 2: Only use the last digit of each number in the sequence. No risk of overflowing


def fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        # Using Way 2. previous and current always stays less than 10. So does newCurrent
        newCurrent = (previous + current) % 10
        previous = current
        current = newCurrent

    return current


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_last_digit(n))
