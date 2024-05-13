import csv
import random
with open('tenk.csv', mode='r') as file:
    csvFile = csv.reader(file)
    lines = list(csvFile)
    random_line = random.choice(lines)
    print(random_line[0])