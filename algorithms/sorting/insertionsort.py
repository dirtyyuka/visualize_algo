def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # key highlighted
        yield arr, {"i": i, "j": i, "action": "compare", "k": None}

        while j >= 0 and key < arr[j]:
            #comparison
            yield arr, {"i": j, "j": i, "action": "compare", "k": j + 1}

            arr[j + 1] = arr[j]

            #shift visualization
            yield arr, {"i": j, "j": i, "action": "sorted"}

            j -= 1

        #insert key
        arr[j + 1] = key

        yield arr, {"i": 0, "j": i, "action": "sorted", "k": None}
