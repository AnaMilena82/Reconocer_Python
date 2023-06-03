num1 = 42  # variable declaration, Numbers
num2 = 2.3 # variable declaration, Numbers
boolean = True # variable declaration, Boolean
string = 'Hello World' # variable declaration, Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, List - initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, Dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, Tuples- initialize
print(type(fruit)) # Tuples access type check
print(pizza_toppings[1]) # List access value
pizza_toppings.append('Mushrooms') # List add value
print(person['name']) #Dictionary access value
person['name'] = 'George' #Dictionary change value
person['eye_color'] = 'blue' #Dictionary add value
print(fruit[2]) # Tuples access value

if num1 > 45: #conditional
    print("It's greater") # function parameter
else: #conditional
    print("It's lower") # function parameter

if len(string) < 5: #conditional
    print("It's a short word!") # function parameter

elif len(string) > 15: #conditional
    print("It's a long word!") # function parameter

else: #conditional
    print("Just right!") # function parameter

for x in range(5): # for loop
    print(x) # function parameter
for x in range(2,5): # for loop
    print(x) # function parameter
for x in range(2,10,3): # for loop
    print(x) # function parameter
x = 0 #variable declaration
while(x < 5): # while loop
    print(x)
    x += 1

pizza_toppings.pop() # function sin parameter
pizza_toppings.pop(1) # function argument

print(person) # function parameter
person.pop('eye_color') # function parameter
print(person) # function parameter

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': #conditional
        continue
    print('After 1st if statement') # function parameter
    if topping == 'Olives': #conditional
        break

def print_hello_ten_times(): # function sin parameter
    for num in range(10): # for loop
        print('Hello') # function parameter

print_hello_ten_times() # function sin parameter

def print_hello_x_times(x): # function parameter
    for num in range(x): # for loop
        print('Hello') # function parameter

print_hello_x_times(4) # function argument

def print_hello_x_or_ten_times(x = 10): # function argument
    for num in range(x): #for loop
        print('Hello') # function parameter

print_hello_x_or_ten_times() # function sin parameter
print_hello_x_or_ten_times(4) # function argument


"""
Bonus section
"""

# print(num3) #NameError: name <variable name> is not defined
# num3 = 72 # variable declaration, Numbers
# fruit[0] = 'cranberry' #change value
# print(person['favorite_team']) #KeyError: 'favorite_team'
# print(pizza_toppings[7]) #IndexError: list index out of range
#   print(boolean) #TypeError: 'tuple' object does not support item assignment
# fruit.append('raspberry') #add value
# fruit.pop(1) #delete value, AttributeError: 'tuple' object has no attribute 'pop'