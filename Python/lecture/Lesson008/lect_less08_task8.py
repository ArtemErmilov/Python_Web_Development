import csv
direct = 'Python/lecture/Lesson008'
with open(f'{direct}/biostats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)
    print(type(line))