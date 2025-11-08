#Implicit Type Casting
x = 10 #int
y = 2.5 # float

sum = x + y # 10.0 + 2.5 = 12.5
print(sum)
print("Type of Sum is:",type(sum))

#Explicit Type Casting
value = "100"  #string
num = int(value)
print("Type of value:",type(num))

f = float(num)
print("Type of f is:",type(f))

price = float(value)
print("Type of f:",type(f))

price = 19.99
price_str = str(price)
print("Price: ",price_str)
print("Type of price_str:",type(price_str))