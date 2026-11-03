print("Name :","Madhesh Gupta ,", "Enrollment_No. :","0863CS231095")

import matplotlib.pyplot as plt
import seaborn as s

week = [1,2,3,4,5,6]   # x axis
silver = [10,30,50,45,52,35]   # y axis
gold = [26,13,57,42,50,45]   # y axis

plt.xlabel("weeks")
plt.ylabel('price')

plt.title('Gold & Silver Rate,\nName : Madhesh Gupta, Enrollment_No. : 0863CS231095')

plt.scatter(week, gold, marker='+', label='gold')
plt.scatter(week, silver, marker='o', label='silver')

'''
plt.scatter(x,y,
            marker='o',
            label='give name')

here marker type can be x, o, +
'''

plt.legend()

plt.savefig('scatter_plot.png')

plt.show()
