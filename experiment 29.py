print("Name :","Madhesh Gupta ,", "Enrollment_No. :","0863CS231095")

import matplotlib.pyplot as plt
import numpy as np

country = ['India', 'Russia', 'America', 'Italy', 'UAE']
d1 = [35,20,30,40,25]

e = [0.2, 0.2, 0, 0.1, 0.1]

plt.pie(
    d1,
    labels=country,
    autopct="%4.2f%%",
    explode=e
)

# plt.pie(d1, labels=country, autopct="%4.2f%%", explode=[0.2,0,0,0.1,0])

plt.title("Name : Madhesh Gupta , Enrollment_No. : 0863CS231095")

plt.savefig("pie_plot.png")

plt.show()
