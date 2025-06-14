def max_loot(capacity, cost_qnty):
    cost_qnty = sort(cost_qnty)
    total_loot = 0
    type_id = 0

    while capacity > 0 and type_id != len(cost_qnty):
        max_amt = min(capacity, cost_qnty[type_id][1])
        unit_price = cost_qnty[type_id][0] / cost_qnty[type_id][1]
        capacity = capacity - max_amt
        total_loot += max_amt * unit_price
        type_id += 1
    return round(total_loot, 3)


def sort(cost_qnty):
    cost_qnty.sort(key=lambda cq: cq[0] / cq[1], reverse=True)
    return cost_qnty


if __name__ == "__main__":
    [type, capacity] = map(int, input().split(" "))
    cost_qnty = []
    for i in range(type):
        [cost, qnty] = map(int, input().split(" "))
        cost_qnty.append([cost, qnty])
    print("{0:.3f}".format(max_loot(capacity, cost_qnty)))
