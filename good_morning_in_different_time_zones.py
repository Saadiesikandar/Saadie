# -*- coding: utf-8 -*-
"""Good Morning in different time zones.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l2CniQK7WzFhnMaotVmL75BhFnEHvCIi
"""

import time
seconds = time.time()
print("seconds since epoch", seconds)

local_time = time.ctime(seconds)
print(local_time)

print (local_time.split())

a = local_time.split()
print(a)

print(local_time)
print (a)
print(type(a))

z , x , c , v , b = a
print(z)
print(x)
print(c)
print(v)
print(b)

print(type(v))

if (v > "00:00:00" and v < "12:00:00"):
  print ("Good Morning")
if (v > "12:00:00" and v < "18:00:00"):
  print ("Good Evening")
if (v > "18:00:00" and v < "23:59:59"):
  print ("Good Night")

q = v.split(":")
print(q)

q1,q2,q3 = q
print(q1)
print(q2)
print(q3)

print(type(q1))

w1=int(q1)
print(w1)

qw1=w1+5
print(qw1)

print(type(qw1))

p=str(qw1)
print(p)

print(type(p))

i=list([p,q2,q3])
u=":".join(i)
print (u)

print(type(u))

if (u > "00:00:00" and u < "12:00:00"):
  print ("Good Morning")
if (u > "12:00:00" and u < "18:00:00"):
  print ("Good Evening")
if (u > "18:00:00" and u < "23:59:59"):
  print ("Good Night")

print ("What is the time in your area:")
your_time=input()
if (your_time > "00:00:00" and your_time < "12:00:00"):
  print ("Good Morning")
elif (your_time > "12:00:00" and your_time < "18:00:00"):
  print ("Good Evening")
elif (your_time > "18:00:00" and your_time < "23:59:59"):
  print ("Good Night")
else:
  print("Error")