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

def group_by_first_letter(words):
    result = {}

    for word in words:
        if not word:
            raise ValueError("Words must not contain empty strings")
        
        first_letter = word[0]

        if first_letter in result:
            result[first_letter].append(word)
        else:
            result[first_letter] = [word]
            
    return result

def find_key_with_highest_value(data):
    if not data:
        raise ValueError("Dictionary cannot be empty")

    highest_key = None
    highest_value = None

    for key, value in data.items():
        
        if highest_value is None:
            highest_key = key
            highest_value = value
        elif value > highest_value:
            highest_key = key
            highest_value = value
            
    return highest_key
