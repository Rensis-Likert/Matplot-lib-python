import matplotlib.pyplot as plt
import numpy as np

# Simulated data: car ages (years) vs car speeds (km/h)
car_age = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
car_speed = np.array([120, 115, 110, 108, 105, 102, 100, 98, 95, 90])

# Scatter plot
plt.scatter(car_age, car_speed, color='blue', s=100, label='Cars')

# Trend line
z = np.polyfit(car_age, car_speed, 1)   # Fit a line (y = mx + b)
p = np.poly1d(z)
plt.plot(car_age, p(car_age), "r--", label='Trend Line')

# Labels and title
plt.xlabel("Car Age (years)")
plt.ylabel("Top Speed (km/h)")
plt.title("Car Age vs Top Speed")
plt.legend()
plt.grid(True)

plt.show()