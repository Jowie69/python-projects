'''========== PYTHON BASICS ========='''
print('Hello World!')
print('Ako si Jowie Flores.')
'''
VARIABLE -  a reusable container for storing a value e.g. x = 21
            a variable behaves as if it were the value it contains.
'''
#declare a value to a variable
age = 21
print(f'You are {age} years old')

#PRINTING METHODS

#print a variable (do not put it in a quote)
#The old fashioned way
print(age)

#Comma Method
print ('You are', age, 'years old')

#String Concatenation Method
print ('You are '+ str(age) +' years old')

#f-string method
print (f'you are {age} years old')

#TIPS & TRICKS
x = 1
y = 2
z = 3

print(x)
print(y)
print(z)

#or MULTIPLE ASSIGNMENT

a, b, c = 4, 5, 6
print(a)
print(b)
print(c)

#ASSIGNING MULTIPLE VARIABLES IN A SINGLE VALUE
d = e = f = 0
print(d)
print(e)
print(f)

'''
======= DIFFERENT DATATYPES: INTEGER, FLOAT, STRING, & BOOLEAN =========
'''
#INTEGER - whole numbers
age = 21
players = 2
quantity = 5

print(f'You are {age} years old')
print(f'There are {players} players online')
print(f'You would like to buy {quantity} items')

#FLOATS - numbers with decimals
gpa = 1.2
distance = 2.5
price = 10.99

print(f'Your gpa is {gpa}')
print(f'You ran {distance}Km')
print(f'The price is ${price}')

#STRING - series of characters/texts
name = "Jowie"
food = "Pizza"
email = 'jowieflores032002@gamil.com'

print(f'Hello {name}!')
print(f'You like {food}')
print(f'Your email is: {email}')

#BOOLEAN - binary, either true or false (Booleans are not enclosed by quotes)

online = True
for_sale = False
running = True

print(f'Are you online?: {online}')
print(f'Is the item for sale?: {for_sale}')
print(f'Game running: {running}')
# ELSE IF
if running:
    print('The game is running')
else:
    print('The game is over')

'''========= TYPE CASTING ==========
    - the process of converting a value of one data type to another
    (string, integer, float, boolean)
'''
#   Explicit vs Implicit
'''====Explicit Type Casting - manually converting values/variables into diff datatypes===='''
name2 = 'Jowie'
age2 = 21
gpa2 = 1.0
student2 = True

print(type(name2))
print(type(age2))
print(type(gpa2))
print(type(student2))
'''
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
'''

#convert integer into a float
age2 = float(age2)
print(age2)
print(type(age2))

#float into an integer
gpa2 = int(gpa2)
print(type(gpa2))

#boolean into a string
student2 = str(student2)
print(type(student2))

#number into a boolean
#note: as a boolean, anything but 0 is True. Meaning, an empty string will result into False
#e.g.
name3 = ''
name3 = bool(name3)
print(name3)
#Running it gives a False result.

age2 = bool(age2)
print(type(age2))

'''=== IMPLICIT TYPE CASTING - automatically changing datatypes'''
x = 2
y = 2.0
#dividing an integer with a  float results into a float output.
x = x/y
print(type(x))
#result: <class 'float'>

'''USER INPUT + EXERCISES'''

#USER INPUT
firstName = input("Enter your name here: ")
age4 = input('Enter your age here: ')
#Here, you'll have to typecast age4 into an int for it to execute the operation.
age4 = int(age4) + 1
#or instead of typecasting, you can use - age = int(input('Enter your age: '))

print("Hi, " + firstName + "!" + " " + "Welcome to Programming 101!")
print(f'So, you are {age4} years old.')
print(f'Have a nice day, {firstName}!')

# ------------------------------------------------
# EXERCISE 1 MAD LIBS
# ------------------------------------------------
adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an adjective: ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw {noun}.")
print(f"{noun} was {adjective2} and {verb}ing.")
print(f"I was {adjective3}!")

# ------------------------------------------------
# EXERCISE 2 AREA CALC
# ------------------------------------------------
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

#area = length * width
#print(f"The area is: {area}cm^2")

# ------------------------------------------------
# EXERCISE 3 SHOPPING CART
# ------------------------------------------------
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${round(total, 2)}")




#CALCULATOR
print("Compute your numbers below: ")
firstNumber = int(input("Enter a Number: "))
secondNumber = int(input("Enter Second Number: "))

result1 = firstNumber + secondNumber
result2 = firstNumber - secondNumber
result3 = firstNumber * secondNumber

print("Addition")
print(str(firstNumber) + " + " + str(secondNumber) + " = " + str(result1))
print("Subtraction")
print(str(firstNumber) + " - " + str(secondNumber)+ " = " + str(result2))
print("Multiplication")
print(str(firstNumber) + " * " + str(secondNumber) + " = " + str(result3))

#USER INPUT
firstName = input("Enter your name here: ")
age4 = input('Enter your age here: ')
print("Hi, " + firstName + "!" + " " + "Welcome to Programming 101!")
print(f'So, you are {age4} years old.')
print(f'Have a nice day, {firstName}!')

#Lists
courses = ["BSIT","BSCS","BSIS","BSCE","BSEE","BSME"]
courses[0] = "BS"
print(courses)
print(courses[0])
print(courses[-2])
print(courses[1:3])
print(courses[:])
print(courses[:4])
print(courses[0:4])

print(len(courses))
