
def binary_search_iterative(source, needle):
    low = 0
    high = len(source) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if source[mid] == needle:
            return mid
        elif source[mid] > needle:
            high = mid - 1
        else:
            low = mid + 1

    return None

def binary_search_recursive(source, low, high, needle):
    if low >= high:
        return None

    mid = int((low + high) / 2)
    if source[mid] == needle:
        return mid
    elif source[mid] > needle:
        return binary_search_recursive(source, low, mid-1, needle)
    else:
        return binary_search_recursive(source, mid+1, high, needle)

lst = [1,2,3,4,5,6,7,8,10]

print(binary_search_iterative(lst, 7))
print(binary_search_recursive(lst, 0, 8, 7))
