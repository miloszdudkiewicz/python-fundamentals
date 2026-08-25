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