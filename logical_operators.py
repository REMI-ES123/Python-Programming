a = 5
b = 3

# and operator
print("a > 2 and b > 1:", a > 2 and b > 1) #True
print("a > 2 and b > 5:", a > 2 and b > 5) #False

# or operator
print("a > 2 or b > 5:", a > 2 or b > 5) #True
print("a < 1 or b < 0 :", a < 1 or b < 0) # False

#not operator
print("not(a > 2):", not(a > 2))
print("not(b > 5):", not(b > 5))

attendence_percentage = 78
cgpa = 8.9
attendence_percentage < 70 or cgpa < 7.5
print(attendence_percentage > 70 and cgpa > 7.5)
print(not(attendence_percentage > 70 and cgpa < 7.5))
