def zeros(number):
    zero_number = 0
    current_number: int = 1

    for i in range(1, number + 1):
        current_number = current_number * i

        last_number = 0
        while last_number == 0:
            last_number = current_number % 10
            current_number = current_number // 10

            if last_number == 0:
                zero_number +=1
            else:
                current_number = last_number
    return zero_number

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7

