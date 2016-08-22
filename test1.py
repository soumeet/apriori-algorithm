import csv
count=[0]*1000
support=[0.0]*1000
LENGTH=0
with open('T10I4D100K.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
    	for i in row:
    		count[int(i)]=count[int(i)]+1
    	LENGTH=LENGTH+1
for i in range(0, LENGTH):
	support[i]=count[i]/LENGTH
min_support=min(support)
