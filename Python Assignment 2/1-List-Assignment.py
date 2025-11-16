
# 1) create a list , accept a number,name and a float value from user and store it inside the list.
#
# now accept one more name from user and insert it at 2nd position.
#
# accept a number and append it at the end of the list.
# print the entire list.

'''
inp1 = int(input("Enter the Integer number: "))
inp2 = input("Enter the Name: ")
inp3 = float(input("Enter the decimal number: "))

mylist = [inp1, inp2, inp3]

inp4 = input("Enter the name to insert at 2nd position: ")
inp5 = int(input("Enter the number to append it at the end: "))
mylist.insert(1,inp4)
mylist.append(inp5)
print(mylist)
'''
# ----------------------------------------------------------------------
# 2) first create list empty. accept numbers till user enters 0 and store them inside the list. Print the list and its length.
#
# Solution ->
'''
mylist = []
inp = int(input("Enter the number: "))
while(inp != 0):
    if(inp==0):
        break
    mylist.append(inp)
    inp = int(input("Enter the number, to stop enter the '0': "))
print(mylist)
print(len(mylist))

'''
# --------------------------------------------------------------------------
# 3) accept 5 numbers, store them inside the list and display it. Now add 3 more numbers [hardcoded] at the end of the list using "extend" method.
#
# Solution ->
'''
mylist = []
i=1
print("Enter the total 5 numbers: ")
while(i <= 5):
    inp = int(input())
    mylist.append(inp)
    i += 1

print(mylist)
mylist.extend([6,7,8])
print(mylist)

'''
# --------------------------------------------------------------------------
# 4) accept a number,string,decimal,boolean value and a character from the user and store it inside the list. First print the list from the beginning and then from the end.
#
# Solution ->
'''
inp_num = int(input("Enter the Integer Number: "))
inp_str = str(input("Enter the Name: "))
inp_float = float(input("Enter the decimal number: "))
inp_bool = bool(input("Enter the anything for True or just press enter for false"))
inp_char = (input("Enter the Single alphabet: "))

mylist = [inp_num, inp_str, inp_float, inp_bool, inp_char]
print(mylist)
print(mylist[::-1])
'''
# ---------------------------------------------------------------------------
# 5) accept 5 numbers, store them inside the list. now accept a number from user which he would like to remove from the list and  after removing it, display the list.
#
# Solution ->

# 6) accept 5 numbers, store them inside the list. now accept a position from user ,remove the element from that position and  after removing it, display the list.
#
# Solution ->

# 7) create a list and store string,number,character,boolean,decimal values respectively inside it.
# Now slice it in following ways:
# a) display it in reverse order
# b) list all the elements from 2nd position
# c) list the elements from 1st to 3rd position
# d) slice it from 1st to 3rd elements from the end.
#
# Solution ->
#
# 8) Note: use List comprehension
#  create a list with the numbers from 1 to 20
#  create one more list which should contain only odd numbers from the first list.
#
# Solution ->
#
# mylist1 = [i for i in range(1, 21)]
# mylist_odd = [i for i in mylist1 if i%2 != 0]
#
# print(mylist1)
# print(mylist_odd)
#
# --------------------------------------------------------------------------
# 9) accept 5 names and store them in list. Now sort the list in ascending order display and then in descending order.
#
# Solution ->
'''
mylist = []
print("Enter the 5 names: ")
for i in range(1,6):
    inp = str(input())
    mylist.append(inp)

print(mylist)
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)
'''
# ---------------------------------------------------------------------------
# 10) create a class "Car" with two instance members i.e. "model(string)" and "isautomatic(boolean)"
# have getter methods also.
# create 5 to 6 objects by passing model name and True or False for "isautomatic".

# create a list and store all the objects inside it.
#
# now create one more list and in that list store all the objects from first list where "isautomatic" is True.
# Print both the lists.

# Solution ->
'''
class Car:
    def __init__(self, name, bool):
        self.name = name
        self.bool = bool

    def __model__(self):
        return self.name
    def __isautomatic__(self):
        return self.bool
    def getname(self):
        return self.name
    def getbool(self):
        return self.bool

    def __str__(self):
        return self.name +"\t \t"+ str(self.bool)
c1 = Car("TATA", True)
c2 = Car("Maruti", True)
c3 = Car("BMW   ", True)
c4 = Car("Audi  ", False)
c5 = Car("Kia   ", False)

mylist = [c1, c2, c3, c4, c5]
print(mylist)

for i in mylist:
    print(i)

new_list = [i for i in mylist if(i.getbool()==True) ]
print("The Automatic cars are: ")
for i in new_list:
    print(i)
'''
