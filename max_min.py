
def max_min(k, arr):
    arr.sort()
    unfairness = float('inf')
    n = len(arr)
    i = 0
    while i + k <= n:
        pairs = arr[i:i+k]
        unfairness = min(unfairness, pairs[-1] - pairs[0])
        i += 1
    return unfairness

def max_min_Optimized(k, arr):
    arr.sort()
    minUnfairness = float('inf')
    i = 0
    while i + k <= len(arr):
        minUnfairness = min(minUnfairness, arr[i + k - 1] - arr[i])
    return minUnfairness
