
def quick_sort(source):
    if len(source) < 2:
        return source

    # choose mid element as pivot for best case scenario (nlogn)
    # or choose random element as pivot for average case scenario (nlogn)
    mid = int(len(source) / 2)
    pivot = source[mid]

    less_than_pivot = [i for i in source if i < pivot]
    greater_than_pivot = [i for i in source if i > pivot]
    equal_to_pivot = [i for i in source if i == pivot]

    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)


def partition(source, low, high):
    mid = int((low + high) / 2)
    i = low - 1
    for j in range(low, high):
        if source[j] < source[mid]:
            i += 1 # everything <= i is less than pivot
            source[i], source[j] = source[j], source[i]
    source[i+1], source[mid] = source[mid], source[i+1]
    return i+1

def quick_sort_inplace(source,low,high):
    if low < high:

        # pi is partitioning index, source[p] is now at right place
        pi = partition(source, low, high)

        # Separately sort elements before partition and after partition
        quick_sort_inplace(source, low, pi-1)
        quick_sort_inplace(source, pi+1, high)

    return source

if __name__ == "__main__":
    # print(quick_sort([4,6,1,3,9,2,6,7]))
    print(quick_sort_inplace([4,6,1,3,9,2,6,7], 0, 7))
