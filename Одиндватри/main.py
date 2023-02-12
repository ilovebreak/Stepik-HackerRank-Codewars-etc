def onetwothree(n):
    tail_symbols = 0
    tail_numbers = 0
    next_tail_symbols = 0
    next_tail_numbers = 0
    i = 0
    while next_tail_symbols < n:
        tail_numbers = next_tail_numbers
        next_tail_numbers += 9 * (10 ** i)
        tail_symbols = next_tail_symbols
        next_tail_symbols += 9 * (10 ** i) * (i + 1)
        i += 1

    previous_number = ((n - tail_symbols) - (n - tail_symbols) % i) + tail_symbols
    if previous_number == n:
        number = int((previous_number - tail_symbols) // i) + tail_numbers
        return int(str(number)[0])

    number = int((previous_number - tail_symbols) // i) + tail_numbers
    next_number = str(number + 1)[::-1]
    result = int(next_number[n - previous_number - 1])
    return result


print(onetwothree(int(input())))
