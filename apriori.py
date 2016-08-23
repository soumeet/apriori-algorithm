import sys
import csv

dataset=sys.argv[1]
min_support=float(sys.argv[2])
transaction=[]
no_of_transaction=0
itemset1_support={}
itemset1_count={}
item_count=[0]*1000
frequent_1itemset=[]
def read_transaction():
	with open(dataset, newline='') as csvfile:
		itemset = csv.reader(csvfile)
		for row in itemset:
			for i in row:
				item_count[int(i)]+=1
			transaction.append(row)

def generate_support():
	for i in range(0, no_of_transaction):
		item_support.append(item_count[i]/no_of_transaction)

def generate_1itemset():
	for i in range(0, no_of_transaction):
		if not item_support[i] == 0.0:
			if item_support[i] >= min_support:
				print(i, ":", item_count[i], ":", item_support[i])

read_transaction()
no_of_transaction=len(transaction)

