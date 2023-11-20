import csv

with open('cleaned.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)

for row in rows:
    if row:
        row[0] = row[0].replace('\n', ' ')

with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
