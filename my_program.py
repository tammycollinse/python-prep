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

#if I had to sum the values of my dictionary together, I would say something like this

mysum = sum(student_grades_dict.values()) #values is a method and sum is function
print(mysum)

#What makes a programmer a programmer
#nknowing syntax, data structures and algorithms

#Tuples are like lists but syntax used is parenthesis
tuesday_temp = (1,2,3)
#what is the true importance of the tuples, they do not have many methods that can mutate and manipulate them
monday_temperatures = [9.1,8.8,7.5]

#more operations with lists
#accessing items with bracket notation works here too
monday_temperatures[1] #finding the value in the list at the index of 1

#slicing has a different syntax in python
monday_temperatures[1:4] # with the numbers making reference to indices of list items
monday_temperatures[0:] #this is the slicing to the end of the list
#we can also use negative indexing in the same way we do in javascript, strings also have indexing 

#accessing items in a dictionary
#we can use bracket notation accessing in order to access items in the dictionary
actors_and_characters = {
    "Chris Evans": "Captain America",
    "Robert Downey Jr" : "Iron Man",
    "Scarlet Johanson": "Black Widow",
    "Mark Ruffallo": "The Hulk"
}

print(actors_and_characters["Robert Downey Jr"])

#creating our own functions

def mean(mylist):
    the_mean = sum(mylist/len(mylist))
    return the_mean

#we invoke functions in the same way
print(mean([1,2,3,4,5])) #this will print the return value of our function

#lets do a currency converter function for USD to ZAR
def currency_converter(amount):
    converted_amount = amount * 17 
    return converted_amount

print(currency_converter(20))

#we are thinking about conditionals and passing parameters as dictionaries etc

#working with the student grades example.

student_grades = {
    "Tammy": 10,
    "Daniel": 9.8,
    "Inge": 8.8,
    "Sandra": 7.7
}

def avg(value):
    if type(value) == dict:
        mean = sum(value.values())/len(value)
    else:
        mean = sum(value)/ len(value)
    
    
    return mean

#how to use user input, there is a input() function that can look like input("Enter temperature:")

#LETS LOOK AT STRING FORMATTING
user_input = input("Please enter your name")
message = f"Hello {user_input}" #this is the newer version of python, this syntax is more readable
print(message)
#remember the .title() method

#for loop, running through the list and then rounding each item
monday_temperatures = [9.1,8.8,7.6]

for temperature in monday_temperatures:
    print(round(temperature))
    print("done")

 #looping through a dictionary
 #you need to specify if you are looping over items, keys or values

#so looping might look something like this

student_grades = {
    "Justin": 8.8,
    "Mary": 10.0,
    "Inge": 5.5
}

for grades in student_grades.items():
    print(grades)


#for loop is executed due to a container
#while loop is based on a condition 

username = " "

while username != "pypy":
    username = input("Enter username: ")
     

#a program that we are going to write

def sentence_maker(phrases):
    interrogatives = ("how", "what" , "why")
    capital = phrases.capitalize()

    if phrases.startswith(interrogatives):
        return "{}?".format(capital)
    else:
        return "{}.".format(capital)


results = []

while True:
    user_input = input("Say something:")
    if user_input == "/end":
        break   
    else:
        results.append(sentence_maker(user_input)) 

print(" ".join((results)))

#list comprehensions , not really sure I understand what is the purpose

temps = [221,234,340,230]

new_temps = []
for temp in temps:
    new_temps.append(temp/10)


print(new_temps)
#we can do this is in a list comprehension

new_temps_list_comp = [temp/10 for temp in temps] # the new list is generated dynamically

#lets look at list comprehensions with conditional statements, the conditional can go inside the list comp
#it will look like this
new_temps_list_comps = [temp/10 for temp in temps if temp != -99999]

#coding exercise 
#Define a function that takes as a parameter a list that contains both integers and strings and returns the list containing only the integers. For example, if I called your function with foo([99, 'no data', 95, 94, 'no data']) it should return [99, 95, 94].
#my solution looks like this

def filter(list):
    only_ints = [item for item in list if type(item) == int]
    return only_ints 

    #if we have an else in a list comprehension, this means that the loop part of the list comp needs to go at the end of the expressiopn

def list_comp(list):
    new_list = [item if type(item) == int else 0 for item in list]
    return new_list

def foo(lst):
    return sum([float(i) for i in lst])

    #functions with multiple arguments/parameters

#having a number of different arguments will look like
#def function_name(*args):
#    return args

def capitalize(*args):
    capitalization = [item.upper() for item in args]
    return sorted(capitalization)

#reading text from a file
file = open("bear.txt")
print(file.read())

#some way to open files and then close them

myfile = open("file.txt")
content = myfile.read()

myfile.close()
print(content) #this will work as the file is now stored in the variable and made reference to the variable
#instead of using the above, you should read text files in the following way below

with open("fruits.txt") as myfile: #myfile in this instance is variable placeholder for 
    cotent = myfile.read()

file = open("bear.txt")
content = file.read()
file.close()
print(content[:90])

def lets_do_this(n):
    if n.mod(3) != 0:
        return "Weird"
    elif n.mod(2) == 0 and (n>=2 and n<=5):
        return "Not weird"
    elif n.mod(2) == 0 and (n>=6 and n<=20):
        return "Weird"
    elif n.mod(2) == 0 and n <20:
        return "Not Weird"

def two_numbers(a,b):
    print(a+b)
    print(a-b)
    print(a*b)


def more_practice(a,b):
    print(a//b)
    print(a/b)

def loops_prac(n):
    for i in range(0,n):
        print(i*i)

def leap_year(year):
    if year%4 == 0:
        return True
    else:
        return False

def looping(num):
    for i in range(1, num+1):
        print(i, end="")

def checking_runner_up(arr):
    winner = max(arr)

    count_for_winner = arr.count(winner)

    for i in count_for_winner:
        arr.remove(winner)
    
    runner_up = max(arr)
    print(runner_up)


    dic = {}
    score_list = list()

    name = input()
    score = float(input())
    
    if score in dic:
        dic[score].append(name)
    else:
        dic[score] = name #this is assigning the key value pair
    if score not in score_list:
        score_list.append(score)

    lowest = min(score)
    score_list.remove(lowest)
    new_low = min(score)
    dic[new_low].sort()

    for i in dic[new_low]:
        print(i)

    # for i in student_marks[query_name]:
    #     s=s+i
    #     print("{0:.2f}".format(s/3))


#ZERO TO MASTERY  COURSE
#formated strings

name = "Tammy"
age = 55
print(f"hi {name}. You are {age} years old")

#when we look at string indexing in python, we have a [start:stop:step over]
#len() counts from one

#booleans

name = "Tammy"
is_cool = True

is_cool = False

 #fundamental data typesd are
 # bool, int , float , complex , str , list , tuple , set , dict

 #This is a password checker exercise using user input

username = input("What is your username")
password = input("What is your password")

password_length = len(password)
password_print = "*" * password_length

print(f"{username}, password {password_print} is {password_length} letters long")

#LISTSSSSSSSSS => one of the important data type, a list of ordered data types , it can have any collection of items that we want

li = [1,2,3,4,5]
li2 = ['a', 'b','c']
li3 = [1,2,'a', True]

#Data Structure is the organization of data to be used with different pros and cons  

#Lets look at list slicing
#we had something like this
string = "hellloooooo"
string[0:2:1] # string[start:stop:step]

amazon_cart = [
    "notebooks",
    "sunglasses",
    "toys",
    "grapes"
]
#wuth slicing, we are creating a copy of the list and can essentially assign it to a new var

amazon_cart[0] = "laptop"
new_cart = amazon_cart[:] #this is syntax that makes a copy instead of assigning a completely new spot in memory
new_cart[0] = "gum"
print(new_cart)
print(amazon_cart)

#MATRIXXXX => An array with another array inside of it, or list with another list inside of it

matrix = [  #also known as a two dimensional array
    [1,2,3],
    [2,4,6],
    [7,8,9]
]

#lets look at LIST METHOOOODDDSSSS

basket = [1,2,3,4,5]
print(len(basket)) #5

#lets look at adding methods ____________________
print(basket.append(100))

basket.insert(4,100) #the first parameter makes reference to the index at which the item is to be inserted ; only modifies the list and does not output a new list
basket.extend(100) #adds to the end of our list, literally extends our list

#lets look at removing methods _____________________
basket.pop() #it pops off the last element in the list if called without an index ; pop also returns the thing that we removed
basket.remove(7) #insert the index that we want to remove
basket.clear #removes whatever is in the list


basket.index(4) #asking where the index of something is and will return the index of that item
#basket.index(what I am looking for , start index , stop index)
print(basket.count(1)) # we will get an output of 1 because the refered to item exists ONCE in our list, it returns numbe rof times item is found in our list

#last couple of methods
basket.sort() #a method that sorts a list || REMEMBER THAT THERE IS A DIFFERENCE BETWEEN METHODS AND BUILT IN FUNCTIONS
basket.reverse() # gives everything the opposite index, it reverses our list 

#LETS TALK ABOUT RANGEEEEE
print(list(range(1,100)))
#.join() is a string method <- it takes in an iterable

#LIST UNPACKING and how it looks

a,b,c , *other = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)
print(other) #=> it prints the remainder of the list omg mind blowwwwwnnn

def test(a):
    '''
    This is known as a doc string that provides information about our function and we can call it like this
    '''

print(test.__doc__) #This will print out that docstring that is written in our function


#lets talk about clean code
def is_even_or_odd(num):
    if num%2 == 0:
        return True
    elif num%2 != 0:
        return False #this is okay considering the method and thinking that one would go through, but the solution below is the cleaner version

#writing this function with cleaner code everyday
def cleanup(num):
    return num%2 == 0

def super_func(*args, **kwargs): #lets lok at args and kwargs
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total_price

print(super_func(1,2,3,4,5, num1=20 , num2=20))
#There is a rule concerning this, params, *args, default parameters, **kwargs

#lets have a look at the walrus operator