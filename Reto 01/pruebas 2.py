numbers: list = [2, 10, 29, 25, 2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 19]


def sum_last_two_numbers(numbers):

    # Sort the list in ascending order
    numbers.sort()
    lenght: int = len(numbers)

    # Sum the last two numbers in the sorted list
    result: int = numbers[lenght - 1] + numbers[lenght - 2]

    print(f"The result is: {result}")


sum_last_two_numbers(numbers)


# Explanation: