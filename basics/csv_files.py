import csv
with open("basics/people.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)