'''
1) define 3 functions "add()","modify()" and "delete()" with just a print message.
now accept input from user as a number. if the number entered is 1, call "add()"
if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]

Solution ->

def add():
    print("add")
def modify():
    print("modify")
def delete():
    print("delete")
print("1 - to add \n 2 - to modify \n 3 - to delete")
inp = int(input("Enter the number: "))

match inp:
    case 1:
        add()
    case 2:
        modify()
    case 3:
        delete()
--------------------------------------------------------------------------

2) define a function which accepts a number and return its square.

Solution ->

def square_num(num):
    return print("The Square of ", num , " is ", num**2)

inp = int(input("Enter the number to find it's Square: \n"))
if inp>0:
    square_num(inp)
else:
    print("Enter number greater than 0 ")
---------------------------------------------------------------------------

3) define a function which accepts character,int,string and display them.

Solution ->

def myfunc1(char, integer, string):
    return print(char, integer, string)

char = str(input("Enter the single Character: \n"))
integer = int(input("Enter the Integer: \n"))
string = str(input("Enter the name: \n"))

myfunc1(char[0], integer, string)

--------------------------------------------------------------------------
4) define "myfun1()" with a print statement. now define "myfun2()" which should invoke "myfun1()" function.
invoke myfun2()

Solution ->

def myfun1():
    print("In myfun1 ")
def myfun2():
    print("In myfun2")
    myfun1()

myfun2()

---------------------------------------------------------------------------
5) define a function to accept a number. This function should return 1 if a number passed is more than 0
return -1 if a number passed is less than 0 , else it should return 0.

Solution ->

def accept_num(num):
    if(num >0):
        return 1
    elif(num<0):
        return -1
    else:
        return 0

print(accept_num(5))
print(accept_num(0))
print(accept_num(-77))

---------------------------------------------------------------------------
6) define a function which accepts a character and return toggle of it.

Solution->

def accept_char(char):
    return print(char.swapcase())

inp = str(input("Enter the Character: \n"))
accept_char(inp[0])

--------------------------------------------------------------------------

7) define a function which accepts a string , toggle and return it.
	[ hint :  use "swapcase()" function of string ]

Solution ->

def accept_char(name):
    return print(name.swapcase())

inp = str(input("Enter the Name: \n"))
accept_char(inp)

--------------------------------------------------------------------------
8) write a function to accept minimum 3 characters and maximum 5 characters.
 	[ use default arguments method ]

Solution ->

def accept(name=""):
    if 3 <= len(name) <= 5:
        print("Accepted:", name)
    else:
        print("Given input name's characters are not in range 3 to 5")

accept()
inp = input("Enter the name (3 to 5 characters): ")
accept(inp)
------------------------------------------------------------------------
9) define a function in such a way that it can accept n number of values and print their sum. [ variable number of arguments]

Solution ->

def arg_sum(*var):
    sum_ = 0
    for i in var:
        sum_ = sum_ + i
    return print(sum_)

arg_sum(1,2,3)
'''