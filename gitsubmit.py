# -*- coding: utf-8 -*-
"""GitSubmit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WzjufnGe0HUDKNoF4ZU-t9TPvQDKyTpc

**Create a program that asks the user to enter their name and their age. Print out a message that tells how many years they have to be 100 years old.**
"""

1)
import datetime
Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
print(Name+" will turn 100 in " +str(datetime.datetime. today().year - Age + 100))


2)
name = input("Enter Your Name:")
age = int(input("Enter Your Age:"))
print("You will Turn 100 in : ",100-age+2022) #Logic =>  100 - 21 (current_Age) = 79 (Final_Age)  +  2022 (current_Year)


3)
from datetime import datetime
name = input('What is your name? \n')
age = int(input('How old are you? \n'))
hundred = int((100-age) + datetime.now().year)
print ('Hello %s. You are %s years old. You will turn 100 years old in %s.' % (name, age, hundred))
