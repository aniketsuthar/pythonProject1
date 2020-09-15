import datetime

print("The current time is ", datetime.datetime.now())

x = 10
y = 10.1
z = "10"

print(type(x), type(y), type(z))

student_grades = [9.6, 20.2, 10.5]

j = list(range(10))
print(j)
f = list(range(1, 10, 2))
print(f)

mysum = sum(student_grades)
length = len(student_grades)
avg = mysum / length
print(avg)
print("max No is ", max(student_grades))

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(student_grades.count(10.0))

username = "Python3"
lowercase = username.lower()
print(lowercase)

student_grades_dict = {"A": 20.0, "B": 32.0, "C": 44.0}
print(sum(student_grades_dict.values()))
print(student_grades_dict.keys())

color_codes = color_codes = ((10, 20, 30), (40, 50, 60), (70, 80, 90))
print(color_codes)

seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
seconds.append(current)
print(seconds)

#  append to List using []

workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])
print(workdays)

print(workdays[:3])
print(workdays[2:])
print(workdays[2:5])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[:3])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[-3:])


# number = float(input("Enter input:"))
# print(number)

# string = input("Enter Greeting: ")
# greeting = f"Hello {string} !"
# print(greeting)

def foo(name):
    return "Hi %s" % name.title()


print(foo("marry"))

phone_numbers = {"A": "123-456-7892", "B": "235-254-1223", "C": "584-745-8585"}

for x in phone_numbers.items():
    print(x)
for key, value in phone_numbers.items():
    print("{}'s phone number is: {} ".format(key, value))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for x in phone_numbers.values():
    print(x.replace("+", "00"))

temps = [221, 'hjghjg', 223, 'jhfjhfhj', 225]


# new_temps = [temp/10 for temp in temps]

# print(new_temps)

def foo_1(temps):
    new_list = [temp for temp in temps if not isinstance(temp, str)]
    return new_list


print(foo_1([23, 'daas', 23, 'asd', 55]))

# Default arguments should follow non-default argument
# 
# def foo_string(*args):
#     new_list = [s.upper() for s in args]
#     return sorted(new_list)


# print(foo_string(["snow","galcier","iceberg"]))    


# Print character occurences in the file

# def foo_read_file(char,path):
#    file = open(path)
#    content = file.read()
#    return  content.count(char)

# print(foo_read_file('a',"bear.txt"))


with open("fruits.txt")  as myFile:
    content = myFile.read()
    myFile.close()
print(content)

# Write to file

with open("vegetables.txt", "w") as veg:
    veg.write("Garlic\nOnions\n")

with open("bear.txt") as myFile:
    content = myFile.read()
    con = content[:90]
    print(con)

with open("first.txt", "w") as writeToFile:
    writeToFile.write(con)

with open("bear1.txt", "r") as readFile:
    content = readFile.read()

with open("bear2.txt", "a") as writeFile:
    writeFile.write(content)

with open("data.txt", "a+") as myFile:
    myFile.seek(0)
    content = myFile.read()
    myFile.seek(0)
    myFile.write(content)

import time
import os

# while True:
#     if os.path.exists("vegetables.txt"):
#
#         with open("vegetables.txt","r") as file:
#             content = file.read()
#             print(content)
#     else:
#         print("File does not exist.")
#     time.sleep(10)


import os
import pandas

while True:
    if os.path.exists("original.csv"):

        with open("original.csv") as file:
            content = pandas.read_csv("original.csv")
            print(content.mean())
    else:
        print("File does not exist.")
    time.sleep(10)
