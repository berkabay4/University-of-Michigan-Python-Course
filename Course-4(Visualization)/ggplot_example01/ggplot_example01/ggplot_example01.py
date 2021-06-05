import matplotlib.pyplot as plt
import matplotlib.style as style

style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.plot(x,y,'g', label = 'line one', linewidth = 2)
plt.plot(x2,y2,'r', label = 'line two', linewidth = 2)

plt.title('Example-01')
plt.ylabel('Y Axis')
plt.xlabel('X Axis')

plt.legend()
plt.grid(True, color = 'black')

plt.show()