
"""
Time Complexity: O(n*2)
Auxiliary Space: O(1)
Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order.
And it takes minimum time (Order of n) when elements are already sorted.
Algorithmic Paradigm: Incremental Approach
Sorting In Place: Yes
Stable: Yes
"""


def insertion_sort(source):
    for i in range(1, len(source)):
        k = source[i]
        j = i - 1
        while j >= 0 and k < source[j]:
            source[j+1] = source[j]
            j -= 1
        source[j+1] = k
    return source

if __name__ == "__main__":
    print(insertion_sort([4,6,1,3,9,2,6,7]))
