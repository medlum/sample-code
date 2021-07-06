# control + F to find code
# ctrl + shft + p for command palette
# run python at terminal and shift + enter to run single line at terminal
# ctrl + alt + n to run code using code runner
# ctrl + J to toggle between terminal
# shft + alt + f to autoformat
# 'sort imports' at command palette 
# install pylinter which is a package in python

# code runner is use for executing codes to see output
# can customised output in settings at user setting, the gear icon
# --> see settings of .vscode folder and click on json icon 
# to run global settings, use command palette : open default settings

# note:
# to run single line in output,
# highlight the code and hit 'ctrl + alt + n'
# however, it runs without memory allocation. 
# so need to run objects with statements 




import math
import os
import sys

a = 1
b = 2
print (a + b)
print(a-b)
print(type(a))
num = 1, 2, 3, 4, 5
sum = 0
for i in num:
    sum = sum+i
print("Total is: ", sum)

#print(sys.version)


# for user input 
# select 'run python in terminal for user input'
# this will run the whole script
# output is just to test
name = input("Your name?")
print('Hello,', name)

