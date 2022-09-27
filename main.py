import csv

with open('./datasets/WorldCupPlayers.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            columns = row
            print(f'Column names are: {columns}')
            line_count += 1
        else:
            if row[6] == "MESSI":
                print(row)

            line_count += 1
    print(f'Processed {line_count} lines.')