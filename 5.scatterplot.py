import matplotlib.pyplot as plt
import numpy as np
months =np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
'Nov', 'Dec'])
affordable_sales = [150, 200, 250, 200, 350, 200, 350, 500, 550, 500, 650, 700]
luxury_sales = [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
super_luxury_sales = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
plt.scatter(months, affordable_sales, color='green', marker="*", label='Affordable Segment')
plt.scatter(months, luxury_sales, color='yellow', marker="s", label='Luxury Segment')
plt.scatter(months, super_luxury_sales, color='blue', marker="p", label='Super Luxury
Segment')
plt.xlabel('Months of Year')
plt.ylabel('Sales of Segments')
plt.title('Sales Data')
plt.legend()
plt.show()



