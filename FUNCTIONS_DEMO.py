# Basic function
def greet():
    print("Welcome to python functions !")
greet()
greet()
greet()

# 2. Greeting with name
def greet_user(name):
    print("Hello, " ,name)

greet_user("Ramesh")
greet_user("Raj")
greet_user("Salman")

#3. Square function
def square(num):
    return num*num

result = square(5)
print("Square:",result)
result = square(6)
print("Square:",result)
print(square(10))
print(square(100))

# maximum of two numbers
def get_max(a, b):
    if a > b:
        return a
    else:
        return b

max_value = get_max(40,30)
print("Maximum:" , max_value)
# calling function inside a loop
def greet_user(name):
    print("Hello, " +name+ "!")

names  = ["Alice", "Bob", "Charlie"]
for name in names:
    greet_user(name)

# functions with default values - Ex. Guest
def greet_default(name ="Guest"):
    print("Hello, " ,name)

greet_default()
greet_default("Ravi")

