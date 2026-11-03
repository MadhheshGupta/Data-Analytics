print("Name :","Madhesh Gupta ,", "Enrollment_No. :","0863CS231095")

import matplotlib.pyplot as plt
import numpy as np

country = ['i', 'c', 'a', 'usa', 'uk']

d1 = [10,20,40,55,35]
d2 = [20,40,60,40,20]
d3 = [30,25,40,28,45]

c = np.arange(len(country))

plt.bar(c, d1, width=0.25, label="gold")
plt.bar(c + 0.25, d2, width=0.25, label="silver")
plt.bar(c + 0.50, d3, width=0.25, label="platinum")

plt.legend()

plt.xlabel("country")
plt.ylabel("Number of Medals")

plt.title("Olympic Medals,\nName : Madhesh Gupta, Enrollment_No. : 0863CS231095")

plt.savefig("bar.png")

plt.show()
