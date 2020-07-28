
def quick_sort(source):
    if len(source) < 2:
        return source

    # choose mid element as pivot for best case scenario (nlogn)
    # or choose random element as pivot for average case scenario (nlogn)
    mid = int(len(source) / 2)
    pivot = source[mid]

    less_than_pivot = [i for i in source if i < pivot]
    greater_than_pivot = [i for i in source if i > pivot]

    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

if __name__ == "__main__":
    print(quick_sort([7,1,3,9,4,6,2]))
