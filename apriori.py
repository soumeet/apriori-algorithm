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
itemset2=[]
itemset2_support={}
itemset2_count={}
frequent_2itemset=[]
itemset3=[]
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

def generate_1itemset():
	for item in itemset:
		itemset_support[item]=float(itemset_count[item]/no_of_transaction)
	for item in itemset:
		if itemset_support[item] >= min_support:
			frequent_1itemset.append(item)

def generate_2itemset():
	for item1 in frequent_1itemset:
		for item2 in frequent_1itemset:
			if not item1==item2:
				if [item2,item1] not in itemset2:
					itemset2.append([item1,item2])
					itemset2_count[item1,item2]=0
	for items in itemset2:
		for row in transactions:
			if set(items).issubset(row):
					itemset2_count[items[0],items[1]]+=1
	for items in itemset2:
		itemset2_support[items[0],items[1]]=float(itemset2_count[items[0],items[1]]/no_of_transaction)
	for items in itemset2:
		if itemset2_support[items[0],items[1]] >= min_support:
			frequent_2itemset.append(items)

read_transactions()
no_of_transaction=len(transactions)
itemset.sort()
generate_1itemset()
generate_2itemset()
print(frequent_2itemset)