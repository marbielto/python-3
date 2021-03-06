# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:11:18 2021

@author: MGB
"""

#string functions
"""
print(", ".join(["spam", "eggs", "ham"]))

print("Hello ME".replace("ME", "world"))

print("This is a sentence.".startswith("This"))

print("This is a sentence.".endswith("sentence."))

print("This is a sentence.".upper())

print("AN ALL CAPS SENTENCE".lower())

print("spam, eggs, ham".split(", "))
"""

#numeric functions
"""
print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))
print(round(2.6))

a = min([sum([11,22]), max(abs(-30),2)])
print(a)
"""

#list functions
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")
    
if any([i%2 == 0 for i in nums]):
    print("At least one is even")
    
for v in enumerate(nums):
    print(v)
    
nums = [-1, 2, -3, 4, -5]
if all ([abs(i)<3 for i in nums]):
    print(1)
else:
    print(2)
    