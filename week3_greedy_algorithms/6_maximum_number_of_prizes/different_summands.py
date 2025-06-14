def maxPrize(prizes):
    i = 1
    while True:
        total = (i * (i + 1)) / 2
        if total == prizes:
            break
        elif total > prizes:
            i -= 1
            break
        else:
            i += 1
    output = []
    for pos in range(i - 1):
        output.append(pos + 1)
        prizes -= pos + 1
    output.append(prizes)
    return i, output


if __name__ == "__main__":
    prizes = int(input())
    result = maxPrize(prizes)
    print(result[0])
    print(" ".join(map(str, result[1])))
