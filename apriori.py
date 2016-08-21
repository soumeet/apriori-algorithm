import sys
import csv

DATASET=sys.argv[1]

with open(DATASET, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
    	print(row)