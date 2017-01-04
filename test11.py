import sys
import csv
import time



dataset=sys.argv[1]
min_support=float(sys.argv[2])
min_confidence=float(sys.argv[3])
transactions=[]
no_of_transactions=0
itemset=[]
itemset_support={}
itemset_count={}
frequent_1itemset=[]
itemset2=[]
itemset2_support={}
itemset2_count={}
itemset2_confidence={}
frequent_2itemset=[]
itemset3=[]
itemset3_count={}
itemset3_support={}
itemset3_confidence={}
frequent_3itemset=[]
rules=[]

def simlr(l1, l2):
        for i in l2:
                i=set(i)
                print(l1, i)
                if set(l1).issubset(i):
                        return True
                else:
                        return False

def read_transactions():
	with open(dataset, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                transactions.append(row[1:])

def generate_1itemset():
	for row in transactions:
		for item in row:
			if item not in itemset:
				itemset.append(item)
				itemset_count[frozenset([item])]=1
			else:
				itemset_count[frozenset([item])]+=1
	for item in itemset:
		itemset_support[frozenset([item])]=float(itemset_count[frozenset([item])]/no_of_transaction)
	for item in itemset:
		if itemset_support[frozenset([item])] >= min_support:
			frequent_1itemset.append(item)

def generate_2itemset():
	for item1 in frequent_1itemset:
		for item2 in frequent_1itemset:
			if not item1==item2:
				if [item2,item1] not in itemset2:
					itemset2.append([item1,item2])
					itemset2_count[frozenset([item1,item2])]=0
	for items in itemset2:
		for row in transactions:
			if set(items).issubset(row):
					itemset2_count[frozenset([items[0],items[1]])]+=1
	for items in itemset2:
                itemset2_support[frozenset([items[0],items[1]])]=float(itemset2_count[frozenset([items[0],items[1]])]/no_of_transaction)
                itemset2_confidence[frozenset([items[0],items[1]])]=float(itemset2_count[frozenset([items[0],items[1]])]/itemset_count[frozenset([items[0]])])
	for items in itemset2:
		if itemset2_support[frozenset([items[0],items[1]])] >= min_support:
			frequent_2itemset.append(items)
		if itemset2_confidence[frozenset([items[0],items[1]])] >= min_confidence:
                        tmp=items[0]+"->"+items[1]
                        rules.append(tmp)

def generate_3itemset():
	'''for item1 in frequent_1itemset:
		for item2 in frequent_1itemset:
			for item3 in frequent_1itemset:
                                print("checking: ",item1," ",item2," ",item3,[item1, item2] in frequent_2itemset and [item2, item3] in frequent_2itemset and [item3, item1] in frequent_2itemset)
                                if [item1, item2] in frequent_2itemset and [item2, item3] in frequent_2itemset and [item3, item1] in frequent_2itemset:
                                        itemset3.append([item1, item2, item3])
                                        itemset3_count[item1, item2, item3]=0
	for item in frequent_1itemset:
		for items in frequent_2itemset:
			items3=[]
			if item not in items:
                                items3=[item, items[0],items[1]]
                                items3.sort()
                                itemset3.append(items3)
                                itemset3_count[frozenset([items3[0],items3[1],items3[2]])]=0'''

	for items1 in frequent_2itemset:
                for items2 in frequent_2itemset:
                        if items1[0]==items2[0]:
                                if not items1[1]==items2[1]:
                                        #print(items1," ",items2,":",items1[0],items1[1],items2[1])
                                        items3=[items1[0],items1[1],items2[1]]
                                        #items3.sort()
                                        for i in itemset3:
                                                print(items3, i)
                                                if set(items3).issubset(i):
                                                        itemset3.append(items3)
                                                        itemset3_count[frozenset([items1[0],items1[1],items2[1]])]=0
	for items in itemset3:
		for row in transactions:
			if set(items).issubset(row):
				itemset3_count[frozenset([items[0],items[1],items[2]])]+=1
	for items in itemset3:
		itemset3_support[frozenset([items[0],items[1],items[2]])]=float(itemset3_count[frozenset([items[0],items[1],items[2]])]/no_of_transaction)
		if not itemset2_count[frozenset([items[1],items[0]])]==0:
                        itemset3_confidence[frozenset([items[0],items[1],items[2]])]=float(itemset3_count[frozenset([items[0],items[1],items[2]])]/itemset2_count[frozenset([items[1],items[0]])])

	for items in itemset3:
		if itemset3_support[frozenset([items[0],items[1],items[2]])] >= min_support:
			print([items[0],items[1],items[2]],itemset3_support[frozenset([items[0],items[1],items[2]])])
			frequent_3itemset.append(items)
'''                                                                                           
		if itemset3_confidence[items[0],items[1],items[2]] >= min_confidence:
                        tmp=items[0]+","+items[1]+"->"+items[2]
                        rules.append(tmp)
                
	for items in itemset3_confidence:
		if itemset3_confidence[items] >= min_confidence:
                        tmp=items[0]+","+items[1]+"->"+items[2]
                        rules.append(tmp)
'''

start_time = time.time()
read_transactions()
no_of_transaction=len(transactions)
print(no_of_transaction)
#print(transactions)

generate_1itemset()
print("Frequent 1-itemset: ", len(frequent_1itemset))
print(frequent_1itemset)

generate_2itemset()
print("Frequent 2-itemset: ", len(frequent_2itemset))
print(frequent_2itemset)

generate_3itemset()
print("Frequent 3-itemset: ", len(frequent_3itemset))
print(frequent_3itemset)
'''
for i in rules:
        print(i)
'''
#print("execution time: %s sec" % (time.time() - start_time))
print("rules generated: ", len(rules))
print("execution time: ", time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))
