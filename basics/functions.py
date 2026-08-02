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
print (find_max([]))   

    