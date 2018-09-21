def insertion_sort(array):
    array_length = len(array)
    # temporally holding cell value
    temp = array[0]
    # pointer to the end of the sorted section. the place in the array
    pointer_sorted = 0
    correct_place_in_array = 0
    while pointer_sorted < array_length - 1:

        if array[pointer_sorted] > array[pointer_sorted + 1]:
            temp = array[pointer_sorted + 1]
            for i in range(pointer_sorted + 1):
                if temp < array[i]:
                    correct_place_in_array = i
                    break

            for i in range(pointer_sorted, correct_place_in_array - 1, -1):
                array[i + 1] = array[i]

            array[correct_place_in_array] = temp
            pointer_sorted += 1
        else:
            pointer_sorted += 1


def main():
    # the provided array
    array = [4, 3, 5, 1, 7, 17, 19, 25, 40, 32, 100, 53]
    print("unsorted array : " + str(array))
    insertion_sort(array)
    print("  sorted array : " + str(array))
    pass


if __name__ == '__main__':
    main()