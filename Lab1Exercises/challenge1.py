# Generate a sequence of integer numbers in the pattern 0, 2, 4, ..., up to 20
# inclusive and display the numbers on the screen.

X = 0
# Your solution here...
while X <= 20:
    print(X)
    X += 2
# Tracing the code :
# it will start with x=0 and then it will check if 0 less than or equal to 20 
# since thats true it will print 0 then increment tha value by 2 
# now x = 2 , it will do the same process until it reaches 20 
# this ocde pronts all the even numbers between 0 and 20 


# Allow the user to enter a string, and then print out each letter
# in the string one at a time on a separate line.

string = input('Enter some text: ')
i = 0
# Your solution here...
while i<= len(string):
    print(string[i])
    i += 1
# input : Diala
# output :
# D
# i 
# a
# l
# a 


# As above, but print out the letters in the string in reverse order.

string = input('Enter some text: ')
# Your solution here...
i = len(string)-1
# print(i)
# Your solution here...
while i>= 0:
    print(string[i])
    i -= 1
# input : Diala
# output :
# a
# l
# a
# i
# D


# Starting with the initial value 0 and 1, generate a Fibonacci sequence.
# Each element in a Fibonacci sequence is the sum of the two previous
# elements e.g. 0, 1, 1, 2, 3, 5, 8, ...
# Allow the user to specify how many elements should be generated.
x = int(input('How many elements? '))
# Your solution here...
first = 0 
second = 1
i = 0 
print(first)
print(second)
for i in range(0,x-2):
    new = first + second
    print(new)
    first = second
    second = new 
    i+=1
# input : number of elements "5"
# output : feb sequence : 0,1,1,2,3

