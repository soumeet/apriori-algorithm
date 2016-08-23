import sys
import csv

dataset=sys.argv[1]
min_support=float(sys.argv[2])
transactions=[]
no_of_transactions=0
itemset=[]
itemset_support={}
itemset_count={}
frequent_1itemset=[]
def read_transactions():
	with open(dataset, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                transaction_row=[]
                for i in row:
                    item=int(i)
                    if item not in itemset:
                        itemset.append(item)
                        itemset_count[item]=1
                    else:
                        itemset_count[item]+=1
                    transaction_row.append(item)
                transactions.append(transaction_row)

def generate_support():
	for item in itemset:
		itemset_support[item]=float(itemset_count[item]/no_of_transaction)

def generate_1itemset():
	for item in itemset:
		if itemset_support[item] >= min_support:
			frequent_1itemset.append(item)

read_transactions()
no_of_transaction=len(transactions)
print(no_of_transaction)
itemset.sort()
generate_support()
generate_1itemset()
print(frequent_1itemset)