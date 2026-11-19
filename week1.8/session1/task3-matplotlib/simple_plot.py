# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "matplotlib",
# ]
# ///
import matplotlib.pyplot as plt

x = [k for k in range(10)]
y_1 = [k**2 for k in x]
y_2 = [k**3 for k in x]

plt.plot(x, y_1)
plt.plot(x, y_2)

plt.xlabel("x")
plt.ylabel("y_1=x^2")
plt.ylabel("y_2=x^3")

plt.show()

# Test the example as is on the slides
# - Modify the data and the range
# - Plot in different ways
# Read matplotlib documentation
# - Test some other plotting functions
