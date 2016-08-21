import sys
import csv

DATASET=sys.argv[1]
no_of_transaction=0
min_support=0.0
item_support=[]
item_count=[0]*1000
with open(DATASET, newline='') as csvfile:
    itemset = csv.reader(csvfile)
    for row in itemset:
    	for i in row:
    		item_count[int(i)]+=1
    	no_of_transaction+=1
for i in range(0, no_of_transaction):
	item_support.append(item_count[i]/no_of_transaction)
print(item_support)