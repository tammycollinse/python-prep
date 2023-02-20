#Conditional logic
is_old = True
is_licenced = True

if is_old and is_licenced:
    print('You are old enough to drive')
     #the indentation after the conditional logic is very very important, everything within that indentation is a part of that code block
elif is_licenced:
    print("This is another condition in the elif being evaluated")
else:
    print("This is checker")


#Lets look at truthy and falsey values, the same rules from JS apply
#lets look at ternary operators, also called conditional expression

#condition_if_true if condition else condition_if_false

is_friend = True
can_messsage = "message allowed" if is_friend else "not friend"

print(can_messsage)

#SHORT CIRCUITING => making reference to OR

if is_friend or  is_licenced:
    print('this is the or operator')

#logical operators ; and or not, == < > 
#Exercise on logical operators

is_magician = False
is_expert = True

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not(is_expert):
    print('At least you are getting there')
elif not(is_magician) and not(is_expert):
    print("You need magic powers")

#IS IS A keyword in python, is checks for the storage and value in memory

#Lets take a look at loops

for item in "Zero To Mastery": #everything after the in keyword should be an iterable, for loop can loop over anything that has iterable content
    print(item)

#whar is an iterable - list, dictionary , tuple , set , string. These items can be checked one by one in their collection

user = {
   "name": "Tammy",
    "age": 5007,
    "can_swim" : False
}

#we are trying to print items in the dictionary

for item in user.items():
    print(item)#This will give us a tuples

for key,value in user.items():
    print(key, value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

counter = 0

my_list = [1,2,3,4,5,6,7,8,9,10]

for item in my_list:
    print(item)
    counter = counter + item
print(f'The total of your list is {counter}')

#Lets look ar range, you can iterate over a range

for number in range(0,100):
    print(number)

for item in range(10,0,-1):
    print(item) #this will be print out in reverse

#enumarate also gives us an index
for i , char in enumerate('Hellllloooooo'):
    print(i, char)

for i, char in enumerate(list(range(0,100))):
    if char == 50:
        print(f"The index of 50 is {i}")

i =0 
while i < 50:
    print(i) #This will be an infinite loop , we would need to increment the i
    i += 1
    break #this will stop the loop
else:
    print('Done with all the work')

my_list = [1,2,3]
for item in my_list:
    print(item)

#the same thing done with a while loop

i = 0

while i < len(my_list):
    print(my_list[i])
    i += 1

while True:
    response = input('Say something: ')
    if response == "Bye":
        break 

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for item in picture:
  for char in item:
    if char == 1:
      print("*" , end='')
    elif char == 0:
      print(" ", end ='')
  print('') #this was pretty cool, it made a christmas tree

  #exercise: check for duplicates in this list

  some_list = ["a", 'b', "c" , 'd' , 'm' , 'n', 'n']
  duplicates = []

  for item in some_list:
      if some_list.count(item) > 1:
          if value not in duplicates:
              duplicates.appened(item)

  print(duplicates)