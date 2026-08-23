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

def merge_dictionaries(dict1, dict2):
    result = {}
    for key, value in dict1.items():
        result[key] = value
    for key, value in dict2.items():
        result[key] = value
        
    return result

def merge_dictionaries_keep_all(dict1, dict2):
    result = {}
    for key, value in dict1.items():
        result[key] = [value]

    for key, value in dict2.items():
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]

    return result