from filereader import file_reader_int
data = file_reader_int("input9.txt")  # Outputs list with all ints


def part1():
    minmax = [0, 25]  # Pointers for array
    next_num = data[minmax[1]]  # Target number
    prev = 0  # Initial value for prev
    while True:
        data_slice = data[minmax[0]:minmax[1]]
        for x in data_slice:
            for y in data_slice:
                if (x+y == next_num):  # If x+y==next, increment pointers
                    minmax[0] += 1
                    minmax[1] += 1
                    next_num = data[minmax[1]]
        if (prev == next_num):  # next_num not changing -> break and return next_num as result
            print(
                "No two pair of numbers among the 25 last numbers sum to {}"
                .format(next_num))
            break
        prev = next_num

    return next_num  # Return invalid num


def part2():
    invalid_num = part1()  # Use result from pt1
    d = 0  # Pointer for minimum index
    u = 1  # Pointer for maximum index

    while True:
        # Increment maximum index pointer until sum > invalid number
        if (sum(data[d:u]) < invalid_num):
            u += 1
        # If sum of range equals invalid number, terminate and print result
        elif (sum(data[d:u]) == invalid_num):
            minmax_sum = min(data[d:u]) + max(data[d:u])
            print("The sum of smallest and largest number in the contigous range that sum up to the invalid number is {}"
                  .format(minmax_sum)
                  )
            break
        else:  # If sum > invalid, increment minimum index pointer and set maximum index pointer to min+1
            d += 1
            u = d+1


part2()
