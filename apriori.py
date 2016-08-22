import sys
import csv

DATASET=sys.argv[1]
no_of_transaction=0
min_support=float(sys.argv[2])
item_support=[]
item_count=[0]*1000
frequent_item1_count=0
with open(DATASET, newline='') as csvfile:
    itemset = csv.reader(csvfile)
    for row in itemset:
    	for i in row:
    		item_count[int(i)]+=1
    	no_of_transaction+=1
for i in range(0, no_of_transaction):
	item_support.append(item_count[i]/no_of_transaction)
#print(item_count)
#print(item_support)

print("item:count:support")
for i in range(0, no_of_transaction):
	if not item_support[i] == 0.0:
		if item_support[i] >= min_support:
			print(i, ":", item_count[i], ":", item_support[i])
			frequent_item1_count+=1
print("frequent 1-itemset: ",frequent_item1_count)