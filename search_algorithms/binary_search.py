def binary_search_by_recursion(x, array):
    ret_val = False
    array_size = len(array)
    mid_array = array_size // 2

    if array[mid_array] == x:
        print("we got our num and its" + str(array[mid_array]))
        return True
    elif array_size > 1:
        if array[mid_array] > x:
            ret_val = binary_search_by_recursion(x, array[:mid_array])
        else:
            ret_val = binary_search_by_recursion(x, array[mid_array:])
    else:
        return False

    return ret_val


if __name__ == '__main__':
    # given array.
    array = [1, 2, 4, 5, 6, 7, 8, 9, 10]

    # checking for correct input.
    x = 0
    invalid_input = True
    while invalid_input:
        x = input("Enter a number: ")
        x = int(x)
        if x < array[0] or x > array[len(array) - 1]:
            print("invalid input, please enter a new num")
        else:
            invalid_input = False

    result = binary_search_by_recursion(x, array)
    if result:
        print("The number you were looking for was found :) ")
    else:
        print("Could not find inout num :( ")
