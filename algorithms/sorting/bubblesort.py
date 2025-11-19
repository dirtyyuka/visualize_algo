def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            yield arr, {"i": j, "j": j+1, "action": "compare", "sorted": i}
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                yield arr, {"i": j, "j": j+1, "action": "compare", "sorted": i}

        if not swapped:
            yield arr, {"i": None, "j": None, "action": "sorted", "sorted": i}
            break
    yield arr, {"i": None, "j": None, "action": "sorted", "sorted": n}
