def selection_sort(arr):
    n = len(arr)
    sorted_count = 0
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            yield arr, {"i": min_index, "j": j, "action": "compare", "sorted": sorted_count}
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
        sorted_count += 1

        #final result
        yield arr, {"i": min_index, "j": i, "action": "compare", "sorted": sorted_count}
    yield arr, {"i": None, "j": None, "action": "sorted", "sorted": sorted_count}