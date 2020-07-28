
"""
Time Complexity: O(n2) as there are two nested loops.
Auxiliary Space: O(1)
The good thing about selection sort is it never makes more than O(n) swaps and can be useful when
memory write is a costly operation.
Stability : The default implementation is not stable. However it can be made stable.
In Place : Yes, it does not require extra space.
"""

def selection_sort(source):
    for i in range(len(source)):
        min_index = i
        for j in range(i + 1, len(source)):
            if source[j] < source[min_index]:
                min_index = j
        source[i], source[min_index] = source[min_index], source[i]
    return source

if __name__ == "__main__":
    print(selection_sort([4,6,1,3,9,2,6,7]))
