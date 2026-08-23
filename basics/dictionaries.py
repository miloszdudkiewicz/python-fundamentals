def count_frequency(numbers):
    frequency = {}

    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    return frequency

print(count_frequency([1, 2, 2, 3, 1, 2]))
print(count_frequency([5, 5, 5]))
print(count_frequency([]))
print(count_frequency([-1, -1, 2]))