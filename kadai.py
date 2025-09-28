import csv
csv_path = 'input.csv'
with open(csv_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if (row[1]) == 'OP02_010':
            print(row[0])