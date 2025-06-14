def lcm(a, b):
    g = gcd(a, b)
    am = a // g
    bm = b // g
    return g * am * bm


def gcd(a, b):
    while True:
        if a == 0 or b == 0:
            break

        if a >= b:
            a = a % b
        else:
            b = b % a

    return b if a == 0 else a


if __name__ == "__main__":
    a, b = map(int, input().split(" "))
    print(lcm(a, b))
