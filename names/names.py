import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

names_1.sort()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_2.sort()

# b2 = BinarySearchTree(names_2[0])
# for n in names_2:
#     b2.insert(n)

# d2 = {}
# for n in names_2:
#     d2[n] = 0

duplicates = []

# # O(n^2) 5.1 seconds
# for name_1 in names_1: # O(n)
#     for name_2 in names_2: # O(n)
#         if name_1 == name_2:
#             duplicates.append(name_1)

# # O(nlog(n)) 0.093 seconds
# for name_1 in names_1: # n
#     if b2.contains(name_1): # log(n)
#         duplicates.append(name_1)

# # O(n) 0.006 seconds
# for name_1 in names_1: # O(n)
#     if name_1 in d2: # O(1)
#         duplicates.append(name_1)

# O(n + m) 0.019 seconds
i1 = 0
i2 = 0
while i1 < len(names_1) and i2 < len(names_2):
    name1 = names_1[i1]
    name2 = names_2[i2]
    if name1 == name2:
        duplicates.append(name1)
        i1 += 1
        i2 += 1
    elif name1 < name2:
        i1 += 1
    else:
        i2 += 1

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

