def is_palindrome(text):
    for index in range(len(text) // 2):
        if text[index] != text[len(text) - 1 - index]:
            return False
    return True

def count_vowels(text):
    counter = 0
    for character in text:
        if character in "aeiouy":
            counter += 1
    return counter