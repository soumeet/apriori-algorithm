import csv
transaction=[]
transaction_part=[]
item=[]
def transactions():
	count=[]
	with open('T10I4D100K.csv', 'rb') as csvfile:
    	 spamreader = csv.reader(csvfile)
    	 for row in spamreader:
    		for i in row:
    			i=int(i)
    			if i not in item:
    				item.append(i)
    			count.append(i)
    		transaction.append(count)
    		count =[]
def partition():
 	size = []
 	c=0
 	for i in range(0,len(transaction)):
 		size[i] = transaction[i].count()
 		for j in range(0,len(transaction)):
 			if size[i] == size[j]:
 				transaction_part[0]=size[i]