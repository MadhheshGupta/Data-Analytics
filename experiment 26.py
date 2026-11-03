print("Name :","Madhesh Gupta ,", "Enrollment_No. :","0863CS231095")

import matplotlib.pyplot as plt
import seaborn as s

week = [1,2,3,4,5,6]   # x axis
silver = [10,40,50,60,35,20]   # y axis
gold = [25,8,23,40,32,45]   # y axis

plt.xlabel("weeks")
plt.ylabel('price')

plt.title('Gold & Silver rate,\nName : Madhesh Gupta, Enrollment_No. : 0863CS231095')

plt.plot(week, gold, label='gold')
plt.plot(week, silver, label='silver')

'''
plt.plot(x,y,
         color_code,
         linewidth = value,
         linestyle = 'dashed',
         marker = 'x',
         label = 'give name')

here linestyle can be dotted, solid, dashed, dashdot
here marker type can be x, o, +
'''

plt.legend()

plt.savefig('line_plot.png')

plt.show()
