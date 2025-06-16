import math


def max_pairwise_product(num_count, num_list):
    # Find the two largest numbers in num_list
    # Their product will be the maximum possible product
    # The indices of the two numbers must be distinct

    # Find the max value and its index in num_list
    max1, max1_index = -math.inf, 0
    for i1 in range(0, num_count):
        if num_list[i1] > max1:
            max1 = num_list[i1]
            max1_index = i1

    # Find the next max value in num_list
    # Its index should not be equal to max1's index
    max2 = -math.inf
    for i2 in range(0, num_count):
        if i2 != max1_index and num_list[i2] > max2:
            max2 = num_list[i2]

    return max1 * max2


if __name__ == "__main__":
    num_count = int(input())
    num_list = list(map(int, input().split(" ")))[0:num_count]
    print(max_pairwise_product(num_count, num_list))
