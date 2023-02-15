#Looking an None as a data type
weapons = None #declaring a variable that has nothing assigned yet

#Lets talk about dictionaries
#It is a data s†ructure in python , it is unordered key value pairs
dictionary = {
    'a': 1 ,
    'b': 2
}

#dictionary keys need to have special properties, needs to be immutable
#it also needs to be unique 

user = {
    "basket": [1,2,3],
    "greet" : "hello",
    "age": 20
}

print(user.get('age')) #this is a dictionary method to get keys from a dictionary
user2 = dict(name = "John") #name is making reference to a var

print("basket" in user) #the expression will return true or false
print("greet" in user.keys())
print("hello" in user.values())
user.popitem() #will remove the last item from the dictionary
user.update({"ages": 55})


#This is our THIRD DATA structure in py
#Tuples are like lists but they are immutable 
my_tuple = (1,2,3,4,5) # you can access the items usinig indices just like a list , there are not many tuple methods

#a tuple only has 2 methods ; count() and index()

#what the hell are sets???

my_set = {1,2,3,4,5} #like a dictionary but no key value pairs, a unique unordered set of objects
#there are no duplicates in a set, everything needs to be unique

#sets methods and why they are useful.

my_set.difference("another set") #it shows which elements are different between two sets
my_set.discard(4) # removes the item passed in from the set

 