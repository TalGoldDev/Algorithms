# finds the n-th Fibonacci number
def fib(number, hash_table):
    val = 0
    if number == 1 or number == 0:
        return number
    else:
        if number - 1 in hash_table.keys():
            val += hash_table[number - 1]
        else:
            hash_table[number - 1] = fib(number - 1, hash_table)
            val += hash_table[number - 1]

        if number - 2 in hash_table.keys():
            val += hash_table[number - 2]
        else:
            hash_table[number - 2] = fib(number - 2, hash_table)
            val += hash_table[number - 2]

    return val


def main():
    # defining a hash table.
    hash_table = {}
    x = input("Enter a number: ")
    print(fib(int(x), hash_table))
    pass


if __name__ == '__main__':
    main()
