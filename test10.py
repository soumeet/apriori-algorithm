import sys
import csv
import time
from collections import Counter
from itertools import combinations

dataset=sys.argv[1]
min_support=float(sys.argv[2])
trans=[]

def read_transactions():
	with open(dataset, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                trans.append(frozenset(row[:]))

def distinct_items(transactions, support=None):
    """Returns counted set of distinct items in transactions"""
    counter = Counter()
    for trans in transactions:
        counter.update(trans)

    if support is not None:
        return set(item for item in counter if counter[item] >= support)
    else:
        return set(counter)

def frequent_single_itemsets(transactions, support):
    """Return one-item itemsets with at least `support` support."""
    distinct = distinct_items(transactions, support)
    return set(frozenset([i]) for i in distinct)

def generate_candidates(L, k):
    """Generate candidate set from `L` with size `k`"""
    candidates = set()
    for a in L:
        for b in L:
            union = a | b
            if len(union) == k and a != b:
                candidates.add(union)
    return candidates

def itemsets_support(transactions, itemsets):
    """Get support for `itemsets`"""

    support_set = Counter()

    for trans in transactions:
        subsets = [itemset for itemset in itemsets if itemset < trans]
        support_set.update(subsets)

    return support_set

def min_support_set(counter, support):
    """Return sets with minimal `support`"""
    items = [item for item in counter if counter[item] >= support]
    return set(items)

def apriori(transactions, support):
    candidates = frequent_single_itemsets(transactions, support)
    result = list()

    k = 2
    while candidates:
        # Get candidate set
        candidates = generate_candidates(candidates, k)
        supported = itemsets_support(transactions, candidates)
        candidates = min_support_set(supported, support)
        result += candidates
        k += 1
        print("k=",k,": ",len(candidates))
        for key,value in supported.items():
                if value > min_support*1000:
                        print(key, value)

    return result


start_time=time.time()
read_transactions()

res=apriori(trans, min_support)
#print(res)

print("execution time: ", time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))

