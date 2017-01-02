import sys
import csv
import time
import numpy as np
from apyori import apriori

dataset=sys.argv[1]
transactions=[] #transactions=[tid, items[]]
no_of_transactions=0


def read_transactions():
	with open(dataset, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                transactions.append(row[1:])

start_time=time.time()
read_transactions()
no_of_transactions=len(transactions)
print(no_of_transactions)
#print(transactions)
results = list(apriori(transactions, 0.001))

#print(results)
for i in results:
    print(i)

print("execution time: ", time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))

