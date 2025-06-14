def change(val):
    count = 0
    coin_size_sorted = [10, 5, 1]
    for size in coin_size_sorted:
        if val >= size:
            count += val // size
            val = val % size
    return count


if __name__ == "__main__":
    m = int(input())
    print(change(m))
