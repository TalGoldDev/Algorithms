# swapping between 2 variables.
def swap(array, left, right):
    temp = array[right]
    array[right] = array[left]
    array[left] = temp
    return 0


def sort(array, current_pivot, left, right):
    while left <= right:
        while array[left] < array[current_pivot]:
            left += 1
        while array[right] > array[current_pivot]:
            right -= 1

        if left <= right:
            swap(array, left, right)
            left += 1
            right -= 1

    # the partition point
    return left


def quick_sort(array, start, end):
    if start >= end:
        return 0

    # choosing a pivot
    current_pivot = (start + (end-start)//2)

    # finding the separation point between the sub-arrays
    partition_point = sort(array, current_pivot, start, end)

    # sorting each of the sub arrays in recursion.
    quick_sort(array, start, partition_point - 1)
    quick_sort(array, partition_point, end)
    return 0


def main():
    # the provided array
    array = [4, 3, 5, 1, 7, 17, 19, 25, 40, 32, 100, 53]
    quick_sort(array, 0, len(array)-1)
    print(array)
    return 0


if __name__ == '__main__':
    main()
