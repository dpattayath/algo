# Complete the pairs function below.
def pairs(k, arr):
    a = set(arr)
    b = set(x + k for x in arr)
    c = a & b
    return len(c)
