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

print(find_sum([]))

    