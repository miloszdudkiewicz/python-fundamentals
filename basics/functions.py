def calculate_average(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)

def find_max(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    
    current_max = numbers[0]

    for number in numbers:
        if number > current_max:
            current_max = number

    return current_max

def find_min(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    
    current_min = numbers[0]

    for number in numbers:
        if current_min > number:
            current_min = number

    return current_min


def find_sum(numbers):
    if not numbers:
        raise ValueError ("To find the sum, the list must contain numbers")
    
    current_sum = 0

    for number in numbers:
        current_sum += number

    return current_sum

def find_second_highest(numbers):
    if len(numbers) < 2:
        raise ValueError("" \
        "To find the second highest, the list must contain at least 2 values"
        )

    highest = numbers[0]
    second_highest = numbers[1]

    if highest < second_highest:
        highest, second_highest = second_highest, highest

    for number in numbers[2:]:
        if number > highest:
            highest, second_highest = number, highest
        elif number < highest and number > second_highest:
            second_highest = number

    return second_highest

def count_occurrences(numbers, to_count):

    counter = 0
    for number in numbers:
        if number == to_count:
            counter += 1
    return counter

def contains(numbers, value):
    for number in numbers:
        if number == value:
            return True
        
    return False

def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number
    return None

def count_above_average(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    
    current_sum = 0
    above_average = 0
    for number in numbers:
        current_sum += number

    average = current_sum / len(numbers)

    for number in numbers:
        if number > average:
            above_average += 1

    return above_average

print(count_above_average([5,5,5,5]))


    
    