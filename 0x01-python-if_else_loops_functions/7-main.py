#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}\n".format("lower" if islower("a") else "upper"))
print("H is {}\n".format("lower" if islower("H") else "upper"))
print("A is {}\n".format("lower" if islower("A") else "upper"))
print("3 is {}\n".format("lower" if islower("3") else "upper"))
print("g is {}\n".format("lower" if islower("g") else "upper"))
