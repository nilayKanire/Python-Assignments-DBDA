# 1)	accept a number and display its table.
from turtledemo.paint import switchupdown
'''
inp = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{inp} * {i} = ", inp*i )
'''
# 2)	using switch ….case   display whether accepted character is vowel or not.

'''Python, unlike many other programming languages, did not traditionally have a built-in switch-case statement. 
However, with the introduction of structural pattern matching in Python 3.10, a match-case statement was added, 
providing similar functionality.'''
"""
inp = input("Enter the character : ")
match inp:
    case "a":
        print("It is Vowel")
    case "e":
        print("It is Vowel")
    case "i":
        print("It is Vowel")
    case "o":
        print("It is Vowel")
    case "u":
        print("It is Vowel")
    case _:
        print("It is not Vowel")
"""
# 3)	Display numbers  1 to 10 using  While loop
'''
i = 1
while(i <= 10):
    print(i)
    i = i+1
'''
# 4)	Display numbers from 3 to 30 except number 24  using while loop.
'''
i = 3
while i <= 30:
    if i==24:
        i = i+1
        continue
    print(i)
    i = i+1
'''
# 5)	accept marks from the user. Using if…….elif….  Else,  display whether result is  fail, pass, second class , first class, Distinction etc.
marks = int(input("Enter the Marks, to see your Remark: "))
if marks >= 75 and marks <= 100:
    print("Distinction")
elif marks >= 60 and marks < 75:
    print("Firs Class")
elif marks >= 40 and marks < 60:
    print("Second Class")
elif marks >34 and marks <40:
    print("Barely Pass")
elif marks > 100:
    print("Invalid Marks")
else:
    print("Fail")

# 6) print the total of first 10 numbers.
# 7) accept numbers till user enters 0 and display the total of all the numbers entered.
# 8) accept a character and display whether it is upper case or lower case or not an alphabet.
# 9) display fibonicii series of 10 numbers
# 10) display prime numbers from 3 to 30
# 11) accept a number and display whether it is prime or not
# 12) print the following pattern:
# *
# * *
# * * *
# * * * *
# * * * * *
#
# 13) print the following pattern:
#
# * * * * *
#
# * * * *
#
# * * *
#
# * *
#
# *
#
# 14) print the following pattern
# 		*
# 	     *  *
#           *  *  *
#        *  *  *  *
#     *  *  *  *  *
#
# 15) print the following pattern
#
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#
#
# 16) print the following pattern
#
# *   *   *   *   *
#
#   *   *   *   *
#
#     *   *   *
#
#       *   *
#
#         *
#
#
# 17) print the following
#
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
