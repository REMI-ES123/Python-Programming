fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

for number in range(1,6):
    print(number)

text = "Hello World"
for letter in text:
    print(letter)

#break statement in for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "apple":
        break
    print(fruit)


#continue statement
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "cherry":
        continue
    print(fruit)