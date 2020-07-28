
def find_smallest(source):
    smallest_index = 0
    smallest_element = source[smallest_index]

    for index, element in enumerate(source):
        if element < smallest_element:
            smallest_element = element
            smallest_index = index
    return smallest_index

def selection_sort(source):
    sorted_source = []
    while (len(source) > 0):
        smallest_index = find_smallest(source)
        sorted_source.append(source.pop(smallest_index))
    return sorted_source

if __name__ == "__main__":
    lst = [4,5,10,5,2,89,10]
    print(selection_sort(lst))
