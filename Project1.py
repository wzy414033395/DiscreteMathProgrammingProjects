#CSIS2430 Spring 2019 SLCC
#Name: Zhengyu Wu
#Project1
#Question 1

import collections
print("\n\n Question 1")
setA = {bin(4), bin(1), bin(2), bin(3)}
setB = {bin(4), bin(5), bin(6), bin(7)}
setC = [4, 1, 2, 3]

def nota(a):
    setX = ['', '', '', '', ]
    for i in a:
        setX[i-1] = bin(0b1111 - a[i-1])
    print("Not Set A is " + str(setX))


def a_and_b(a, b):
    print("Set A and B is " + str(a.union(b)))


def a_minus_b(a, b):
    print("Set A - B is " + str(a.difference(b)))


def a_xor_b(a, b):
    print("Set A xor B is " + str(a.symmetric_difference(b)))


print("Set A is " + str(setA))
print("Set B is " + str(setB))
nota(setC)
a_and_b(setA, setB)
a_minus_b(setA, setB)
a_xor_b(setA, setB)


#Question 2
print("\n\n Question 2")
multisetA = collections.Counter({'a': 3, 'b': 2, 'c': 1})
multisetB = collections.Counter({'a': 2, 'b': 3, 'd': 4})
print("Multi set A is " + str(multisetA))
print("Multi set B is " + str(multisetB))
print("Multi set A union Multiset B is " + str(multisetA | multisetB))
print("Multi set A intersection B is " + str(multisetA & multisetB))
print("Multi set A minus B is " + str(multisetA - multisetB))
print("Multi set A plus B is " + str(multisetA + multisetB))

print("\n\n Question 3")
fuzzysetA = collections.Counter({'Alice': 0.6, 'Brian': 0.9, 'Fred': 0.4, 'Oscar': 0.1, 'Rita': 0.5})
fuzzysetB = collections.Counter({'Alice': 0.4, 'Brian': 0.8, 'Fred': 0.2, 'Oscar': 0.9, 'Rita': 0.7})
fullset = collections.Counter({'Alice': 1, 'Brian': 1, 'Fred': 1, 'Oscar': 1, 'Rita': 1})

print("Fuzzy set not A is " + str(fullset - fuzzysetA))
print("Fuzzy set A union fuzzy set B is " + str(fuzzysetA | fuzzysetB))
print("Fuzzy set A intersection fuzzy set B is " + str(fuzzysetA & fuzzysetB))
