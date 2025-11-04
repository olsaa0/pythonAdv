my_set = {1, 2, 3}
my_set = set()
my_set = set([4, 5, 6])

print(my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_result_method = set1.union(set2)

union = set1 | set2

print("Union: ", union_result_method)
print("Union method: ", union)

intersection = set1 & set2
print("intersection method: ", intersection)

method = set1 - set2
print("difference method: ", method)

symmetrical_difference = set1 ^ set2
print("symmetrical_difference method: ", symmetrical_difference)