import csv

with open('data/example1.csv', 'r') as f:
    reader = csv.DictReader(f)

    print(reader)

    print('Line nums', reader.line_num)
    print('Dialect', reader.dialect)
    for row in reader:
        print(row)
        # row['name'] --> row[0]
