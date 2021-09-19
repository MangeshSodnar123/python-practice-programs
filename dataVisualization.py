from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x = [1,2,5]
y = [4, 5, 6]
plt.plot(x, y, 'g', label='line one', linewidth=5)
plt.title("Data Visulization")
plt.ylabel("y axis")
plt.xlabel("x axis")
plt.legend()
plt.grid(True,color='k')
plt.show()