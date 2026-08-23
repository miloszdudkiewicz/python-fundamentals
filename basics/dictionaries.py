def count_frequency(numbers):
    frequency = {}

    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    return frequency

def invert_dictionary(data):
    inverted = {}
    for key, value in data.items():
        inverted[value] = key
    return inverted
