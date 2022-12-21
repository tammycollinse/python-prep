print(3+4)
#the math operations are the same as JS
print(117 + 986)
print(199 - 981)

#variables

spent = 3
donated = 4
total_amount = spent + donated
print(total_amount)

#we could also have something like this

items = 2
price = 12

total_price = items * price
print(total_price)
#printing multiple variables syntax print(var1,var2,var3)

#lists are the equivalent of arrays. Called lists

student_grades = [4.3,8.9,6.7] #different data types can be stored in the lists
print(student_grades)
print(student_grades * 3) #this will print the entire list 3 times, this is really cool lol
#there is a range data type range(0,11) //if you convert this into a list, you will be able to see its significance
range(0,11) # first parameter being start, the second parameter being stop (one prior)
#range(start, stop, step), range syntax

x = range(0,20) # I can use x as a loop reference

#if we use dir(add_data_type_here), it will show you a list of methods that can be called on those specific data types
#dir(float), dir(list)

mysum = sum(student_grades)

#to get a complete list of functions that are available in python, you can say dir(__builtins__)
length_of_list = len(student_grades)
mean = sum/length_of_list

print(student_grades.count("item to match"))

#A dictionary is the equivalent of an object but is also made up of key value pairs

student_grades_dict = {
    "Mary": 9.0,
    "Sim": 2.3,
    "Tammy": 10
}