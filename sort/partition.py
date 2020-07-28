
def partition(source):
    low = 0
    high = len(source) - 1

    mid = int((low + high) / 2)

    i = low - 1
    for j in range(low, high):
        if source[j] < source[mid]:
            i += 1 # everything <= i is less than pivot
            source[i], source[j] = source[j], source[i]
    source[i+1], source[mid] = source[mid], source[i+1]
    return source

if __name__ == "__main__":
    print(partition([2,4,6,1,3,9,2,6,7]))
