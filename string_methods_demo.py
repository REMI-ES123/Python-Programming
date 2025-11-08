#lower
original = "Hello World"
lowered = original.lower()
print("Lowercase:", lowered)

#upper method
upper = lowered.upper()
print("Uppercase:", upper)

#strip() method
messy = "   Python   "
cleaned = messy.strip()
print("After strip:", cleaned)

#replace()  method
text = "Java is powerful"
updated = text.replace( "Java", "Python" )
print("After replace:", updated)

#split() method
sentence = "Python is easy to learn"
words = sentence.split( )
print("Split result:", words)

#find() method
text = "Learning Python is fun"
position = text.find( "Python" )
print("Found at position:", position)

#Title() method
heading = "Welcome to Python programming"
formatted = heading.title()
print("Title case:", formatted)

# capitalize() method
msg = "hello WORLD"
cleaned = msg.capitalize()
print("capitalize:" , cleaned)

# startswith() method
greeting = "Hello everyone"
print(greeting.startswith("Hello"))
print(greeting.startswith("Hi"))

#endswitch() method
print(greeting.endswith("everyone"))
print(greeting.endswith("Hello"))

# count() method
sentence = "Python is easy . Python is powerful. Python is popular."
count = sentence.count("Python")
print("total count:", count)

#isalpha() method
name = "Python"
print(name.isalpha())
