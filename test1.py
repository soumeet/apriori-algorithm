import csv
count=[0]*1000 
print (count)
with open('T10I4D100K.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    mx=0
    for row in spamreader:
    	mx=max(row)
    print("max: ", mx)