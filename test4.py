import csv

transaction=[]
support={}
support2={}
support3={}
frequent=[]
item=[]
item2=[]
min_support=3
def transactions():
	count=[]
	with open('T10I4D100K.csv', 'rb') as csvfile:
    	 spamreader = csv.reader(csvfile)
    	 for row in spamreader:
    		for i in row:
    			i=int(i)
    			if i not in item:
    				item.append(i)
    				support[i]=1
    			else:
    				support[i] += 1
    			count.append(i)
    		transaction.append(count)
    		count =[]
    		item.sort()


def first_frequent():
	for i in item:
		if support[i]>3:
			frequent.append(i)
	
def sec_freq():
	c=0
	k=0
	l=0
	for i in range(0,len(frequent)-1):
		for j in range(i+1,len(frequent)-1):
			item2.append([frequent[i],frequent[j]])
			support2[frequent[i],frequent[j]]=0
	for b in range(0,len(item2)):
		for i in range(0,len(transaction)):
			
			if item2[b][0] in transaction[i]:
				c+=1
			if item2[b][1] in transaction[i]:
				c+=1
			if c==2:
				k=item2[b][0]
				l=item2[b][1]
				support2[k,l]+=1
				
			c=0
	
	for b in range(0,len(item2)-1):
		k=item2[b][0]
		l=item2[b][1]
		if support2[k,l]>3:
			print item2[b]
			print support2[k,l]
		else:
			del support2[k,l]	
def tre_frec():
	c=0
	item3=[]
	z=0
	k=0
	l=0
	for i in range(0,len(frequent)-1):
		for j in range(i+1,len(frequent)-1):
			for m in range(j+1,len(frequent)-1):
				k=frequent[i]
				l=frequent[j]
				n=frequent[m]
				if (k,l) in support2 and (l,n) in support2 and  (k,n) in support2:
					item3.append([frequent[i],frequent[j],n])
					support3[frequent[i],frequent[j],frequent[m]]=0
	
	for b in range(0,len(item3)):
		for i in range(0,len(transaction)):
			
			if item3[b][0] in transaction[i]:
				c+=1
			if item2[b][1] in transaction[i]:
				c+=1
			if item3[b][2] in transaction[i]:
				c+=1
			if c==3:
				k=item3[b][0]
				l=item3[b][1]
				n=item3[b][2]
				support3[k,l,n]+=1
			c=0
	
	for b in range(0,len(item3)-1):
		k=item3[b][0]
		l=item3[b][1]
		n=item3[b][2]
		if support3[k,l,n]>3:
			print item3[b]
			print support3[k,l,n]
		else:
			del support3[k,l,n]	


transactions()
first_frequent()
sec_freq()
tre_frec()
