import matplotlib.pyplot as plt

departments = ["IT", "Finance","HR"]
salaries = [60000, 70000, 50000]

plt.bar(departments, salaries, color = ["blue", "green", "orange"], width=0.5)
plt.title("Average Salaries by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()

plt.barch(departments, salaries, color ="purple")
plt.title("Average Salaries by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()
