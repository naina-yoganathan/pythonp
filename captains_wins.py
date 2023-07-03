import csv
with open("captains.txt") as FH:
    data = csv.reader(FH)
    header = next(data)
    for row in data:
        print(f"{row[0]:14} {row[3]:>3}")



