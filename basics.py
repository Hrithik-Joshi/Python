#Integers and floats
age = 25
height = 3.9

#Strings -> work as arrays
name = "Hrithik"
greeting = "hello" + name
print(name[1])
print(len(name))

#List and tuple
numbers = [1,2,3]
names = ["hrithik", "Joshi"]
coordinate = (1,2)
coordinates = tuple((1,2))

#Dictionary
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(key,value)

#Booleans
is_student = False

#Control flow
num = 10
if num > 0:
    print("positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")   
    
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
#for loop with range
for i in range(3):
    print(i)
for i in range(2,10):
    print(i)
for i in range(3,30,3):
    print(i)  
    
#user input
num = int(input("Enter a num:"))

if num > 1:
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is a prime number")
    

#functions
def my_func(a):
    print(a)
my_func(5)

#Positional- Only Argument
def func1(a, /):
    print(a)
func1(3)

#Keyword only args
def func2(*,a,b):
    print(a+b)
func2(a=1,b=2)

#split
word = "hello, how are you"
print(word.split(","))