def count_file_lines(file_path):
    counter = 0

    with open(file_path, "r") as file:
        for line in file:
            counter += 1

    return counter

def read_file_content(file_path):
    with open(file_path, "r") as file:
        file_text = file.read()

    return file_text

def write_file_content(file_path, text):
    with open(file_path, "w") as file:
        file.write(text)

def append_file_content(file_path, text):
    with open(file_path, "a") as file:
        file.write(text + "\n")

def analyze_file(file_path):
    word_counter = 0
    char_counter = 0
    line_counter = 0
    with open(file_path, "r") as file:
        for line in file:
            line_counter += 1
            char_counter += len(line)
            word_counter += len(line.split())
    return {
        "lines": line_counter,
        "words": word_counter,
        "characters": char_counter
    }

def find_longest_line(file_path):
    longest_length = 0
    longest_line_number = 0
    longest_line = ""
    with open(file_path, "r") as file:
        for line_number, line in enumerate(file, start=1):
            if len(line.strip()) > longest_length:
                longest_length = len(line.strip())
                longest_line_number = line_number
                longest_line = line.strip()

    return longest_line, longest_line_number