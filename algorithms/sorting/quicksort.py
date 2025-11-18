def quick_sort(arr, low=0, high=None, placed=None):
    if placed is None:
        placed = set()

    if high is None: high = len(arr) - 1

    if low >= high:
        yield arr, {"i": None, "j": None, "action": "sorted", "k": None, "placed": placed}
        return

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            # highlight comparison
            yield arr, {"i": j, "j": high, "action": "compare", "k": i, "placed": placed}

            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

                #highlight swap
                yield arr, {"i": j, "j": high, "k": i, "action": "compare", "placed": placed}

        # final swap
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        placed.add(i + 1)
        yield arr, {"i": low, "j": high, "action": "sorted", "k": None, "placed": placed}
        return i + 1

    gen = partition(arr, low, high)

    try:
        while True:
            value = next(gen)
            yield value
    except StopIteration as e:
        pivot_index = e.value

    yield from quick_sort(arr, low, pivot_index - 1, placed)
    yield from quick_sort(arr, pivot_index + 1, high, placed)

    if low == 0 and high == len(arr) - 1:
        all_sorted = set(range(len(arr)))
        yield arr, {"i": None, "j": None, "action": "sorted", "k": None, "placed": all_sorted}
