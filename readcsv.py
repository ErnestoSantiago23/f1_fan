import csv

with open ('raw_data/circuits.csv') as csvcircuits:
    reader = csv.DictReader(csvcircuits, skipinitialspace=True)
    for row in reader:
        print(type(row))
