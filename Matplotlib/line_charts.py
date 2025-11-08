import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
visit = [250, 270, 300, 280, 350, 400, 420]

plt.plot(days, visit)
plt.title("Website Traffic Over a Week")
plt.xlabel("Days of the week")
plt.ylabel("Number of visitors")
plt.show()

plt.plot(days, visits, color ="blue", linestyle = "--", linewidth = 2)
plt.title("Website Traffic Over a Week")
plt.xlabel("Days of the week")
plt.ylabel("Number of visitors")
plt.show()


