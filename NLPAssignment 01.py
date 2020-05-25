# -*- coding: utf-8 -*-



#1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple
#of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
#comma-separated sequence on a single line.

a = []
for i in range(2000,3500):
    if (i % 7) == 0 and (i % 5 == 0):
        a.append(str(i))
print(a)
  
      
#2.Write a Python program to accept the user's first and last name and then getting them printed in
#the the reverse order with a space between first name and last name. 

First_name = input("Enter the First Name")
Last_name = input("Enter the Last Name ")

print(First_name ,"",Last_name)
    
#3.Write a Python program to find the volume of a sphere with diameter 12 cm.
#Formula: V=4/3 * π * r

Diameter = 12
radius = Diameter/2
exponential = pow(radius,3)

volume = (4/3) * 3.141592 * exponential 
print (volume)
