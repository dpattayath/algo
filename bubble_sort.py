
def bubble_sort(source):
    for i in range(0, len(source)):
        swap = 0
        for j in range(i+1, len(source)):
            if source[i] > source[j]:
                source[i], source[j] = source[j], source[i]
                swap = 1
        if not swap:
            break

    return source

if __name__ == "__main__":
    lst = [4,5,10,5,2,89,10]
    print(bubble_sort(lst))
