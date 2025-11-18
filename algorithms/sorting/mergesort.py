def merge_sort(arr, low=0, high=None):
    if high is None: high = len(arr) - 1

    if low >= high:
        return

    mid = (low + high) // 2

    # left half
    yield from merge_sort(arr, low, mid)
    # right half
    yield from merge_sort(arr, mid + 1, high)

    # merge
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]

    i = j = 0
    k = low

    while i < len(left) and j < len(right):
        yield arr, {"i": low, "j": high, "action": "compare", "k": k, "a": low + i, "b": mid + 1 + j}

        if left[i] < right[j]:
            arr[k] = left[i]
            yield arr, {"i": low, "j": high, "action": "compare", "k": k + 1, "a": None, "b": mid + 1 + j}
            i += 1
        else:
            arr[k] = right[j]
            yield arr, {"i": low, "j": high, "action": "compare", "k": k + 1, "a": None, "b": mid + 1 + j}
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        yield arr, {"i": low, "j": high, "action": "merged", "k": k + 1, "a": None, "b": None}
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        yield arr, {"i": low, "j": high, "action": "merged", "k": k + 1, "a": None, "b": None}
        k += 1

    yield arr, {"i": low, "j": high, "action": "merged", "k": k, "a": None, "b": None}
