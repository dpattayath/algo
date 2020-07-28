

def binary_search(source, needle):
    low = 0
    high = len(source) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = source[mid]

        if (guess == needle):
            return mid
        elif (guess < needle): # guess is too low
            low = mid + 1
        else: # guess is too high
            high = mid - 1

    return None

if __name__ == "__main__":
    lst = [2,3,9,12,23,45,78,90]
    print(binary_search(lst, 78))
