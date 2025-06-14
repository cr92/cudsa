def binary_search(arr_size, arr, query):
    start = 0
    end = arr_size - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == query:
            return mid
        if arr[mid] > query:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def bs(arr_size, arr, query_size, queries):
    output = []
    for i in range(query_size):
        output.append(binary_search(arr_size, arr, queries[i]))
    return " ".join(map(str, output))


if __name__ == "__main__":
    num_keys = int(input())
    input_keys = list(map(int, input().split(" ")))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    queries = list(map(int, input().split(" ")))
    assert len(queries) == num_queries

    print(bs(num_keys, input_keys, num_queries, queries))
