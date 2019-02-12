#CSIS2430 Spring 2019 SLCC
#Name: Zhengyu and Gordan
#Project1
#Question 1

import collections
print("\n\n Question 1")
setA = {bin(4), bin(1), bin(2), bin(3)}  # create set A of binary numbers
setB = {bin(4), bin(5), bin(6), bin(7)}  # create set B of binary numbers
setC = [4, 1, 2, 3]


def nota(a):  # create a function for not A
    setX = ['', '', '', '', ] # empty lists of size four
    for i in a:
        setX[i-1] = bin(0b1111 - a[i-1])  # Use 0b1111 minus the input set to get the not set
    print("Not Set A is " + str(setX))


def a_and_b(a, b):  # create a function for taking two sets and output a union of them
    print("Set A and B is " + str(a.union(b)))


def a_minus_b(a, b): # create a function for taking two sets and output a subtraction of them
    print("Set A - B is " + str(a.difference(b)))


def a_xor_b(a, b):  # create a function for taking two sets and output aor of them
    print("Set A xor B is " + str(a.symmetric_difference(b)))


print("Set A is " + str(setA))  # print the original set A
print("Set B is " + str(setB))  # print the original set B
nota(setC)  # Use of the not A function
a_and_b(setA, setB)  # Use of the union function
a_minus_b(setA, setB)  # Use of the minus function
a_xor_b(setA, setB)  # use of the xor function


#Question 2
print("\n\n Question 2")
multisetA = collections.Counter({'a': 3, 'b': 2, 'c': 1})  # Create multi set A with collections
multisetB = collections.Counter({'a': 2, 'b': 3, 'd': 4})  # Create multi set B with collections
print("Multi set A is " + str(multisetA))  # print the multi set A
print("Multi set B is " + str(multisetB))  # print the multi set B
print("Multi set A union Multiset B is " + str(multisetA | multisetB))  # print the multi set A union with multi set B
print("Multi set A intersection B is " + str(multisetA & multisetB))  # print the multi set A intersection with multi set B
print("Multi set A minus B is " + str(multisetA - multisetB))  # print the multi set A minus with multi set B
print("Multi set A plus B is " + str(multisetA + multisetB))  # print the multi set A plus with multi set B

print("\n\n Question 3")
fuzzysetA = collections.Counter({'Alice': 0.6, 'Brian': 0.9, 'Fred': 0.4, 'Oscar': 0.1, 'Rita': 0.5})  # Create fuzzy set A
fuzzysetB = collections.Counter({'Alice': 0.4, 'Brian': 0.8, 'Fred': 0.2, 'Oscar': 0.9, 'Rita': 0.7})   # Create fuzzy set B
fullset = collections.Counter({'Alice': 1, 'Brian': 1, 'Fred': 1, 'Oscar': 1, 'Rita': 1})  # create a full fuzzy set with everything to 1

print("Fuzzy set not A is " + str(fullset - fuzzysetA))  # the not A set is use the full set minus the set A
print("Fuzzy set A union fuzzy set B is " + str(fuzzysetA | fuzzysetB))  # The union of set A and B
print("Fuzzy set A intersection fuzzy set B is " + str(fuzzysetA & fuzzysetB))  # The intersection of set A and B
