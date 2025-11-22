# 1) Write a Python program to count the elements in a list until an element is a tuple.
#
# Sample input : list = [10, 20, 30, (40,50), 60]
# Sample output = 3
'''
mylist = [10,20, 30, (40,50), 60]
print(type(mylist[3]))
count = 0
for i in mylist:
    if type(i) is tuple:
        break
    else:
        count = count + 1
print(count)
'''
# 2) create a tuple to store 5 numbers and then sort it in ascending and descending order.

tup = (1, 5, 3, 2, 4)
# ascending
asc_tup = sorted(tup)
print(asc_tup)

# descending
desc_tup = sorted(tup,reverse=True)
print(desc_tup)

# 3) Write a Python program to find the repeated items of a tuple.






