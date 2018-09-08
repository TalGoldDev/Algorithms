# input : array of N different numbers.
# output : sorted array.


def merge_halves(array, left_start, right_end, temp_array):
    mid_array = (left_start + right_end) // 2
    right_start = mid_array + 1  # starting position of right array
    array_size = right_end - left_start + 1

    left_iterator = left_start
    right_iterator = right_start

    temp_index = left_start

    # sorting out the elements between the subarrays
    while left_iterator <= mid_array and right_iterator <= right_end:
        if array[left_iterator] <= array[right_iterator]:
            temp_array[temp_index] = array[left_iterator]
            left_iterator += 1
        else:
            temp_array[temp_index] = array[right_iterator]
            right_iterator += 1

        temp_index += 1

    # adding array elements that got left behind
    while left_iterator <= mid_array:
        temp_array[temp_index] = array[left_iterator]
        left_iterator += 1
        temp_index += 1

    # adding array elements that got left behind
    while right_iterator <= right_end:
        temp_array[temp_index] = array[right_iterator]
        right_iterator += 1
        temp_index += 1

    # copying back the sorted sub array to our original array.
    for i in range(0, array_size):
        array[left_start+i] = temp_array[left_start+i]

    pass


def merge_sort(array, left_start, right_end, temp_array):
    mid_array = (left_start + right_end) // 2
    if left_start >= right_end:
        return

    merge_sort(array, left_start, mid_array, temp_array)
    merge_sort(array, mid_array + 1, right_end, temp_array)

    merge_halves(array, left_start, right_end, temp_array)

def main():
    # the provided array
    array = [4, 3, 5, 1, 7, 17, 19, 25, 40, 32, 100, 53]
    temp_array = [0] * (len(array))

    merge_sort(array, 0, len(array)-1, temp_array)

    print(array)

    return 0


if __name__ == '__main__':
    main()
