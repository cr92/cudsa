def max_revenue(slots, prices, clicks):
    revenue = 0
    prices.sort()
    clicks.sort()
    for i in range(slots):
        revenue += prices[i] * clicks[i]
    return revenue


if __name__ == "__main__":
    slots = int(input())
    prices = list(map(int, input().split(" ")))
    clicks = list(map(int, input().split(" ")))
    assert len(prices) == len(clicks) == slots
    print(max_revenue(slots, prices, clicks))
