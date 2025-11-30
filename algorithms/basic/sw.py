def slidingwindow(data, target):
    sum = count = 0
    idx = -1
    n = len(data)
    yield data, {"i": -1, "j": -1, "sum": sum, "count": count}
    for i in range(n):
        sum += data[i]
        yield data, {"i": idx, "j": i, "sum": sum, "count": count}

        # ------ keep sum <= target ------
        while idx <= i and sum > target:
            idx += 1
            sum -= data[idx]
            yield data, {"i": idx, "j": i, "sum": sum, "count": count}

        count += 1 if sum == target else 0
        yield data, {"i": idx, "j": i, "sum": sum, "count": count}
    
    return count