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
print(analyze_file("basics/test1"))