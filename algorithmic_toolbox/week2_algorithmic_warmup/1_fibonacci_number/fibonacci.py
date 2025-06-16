# [0,1,1,2,3,5,8,...], Oth Fiboncci 0


# This version use O(n) extra space to store the generated Fibonacci sequence in a list.
def fibonacci_number_v1(n):
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list[n]


# No need to store the entire sequence as only the Nth number is required. Uses O(1) space.
def fibonacci_number_v2(n):
    if n <= 1:
        return n

    prev, curr = 0, 1
    for i in range(2, n + 1):
        prev, curr = curr, curr + prev
    return curr


if __name__ == "__main__":
    input_n = int(input())
    print(fibonacci_number_v2(input_n))
