import numpy as np
import matplotlib.pyplot as plt
import math

# #### **1. Basic Plotting**
# - **Task**: Plot the function $ f(x) = x^2 - 4x + 4 $ for $ x $ values between -10 and 10. Customize the plot with appropriate labels for the axes and a title.

x = np.linspace(-10, 10, 200)  # 200 points for a smooth curve
y = x**2 - 4*x + 4

plt.plot(x, y, linestyle='--', color='blue')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Quadratic Function: f(x) = x² - 4x + 4')
plt.grid(True)
plt.show()

# ---

# #### **2. Sine and Cosine Plot**
# - **Task**: Plot $ \sin(x) $ and $ \cos(x) $ on the same graph for $ x $ values ranging from 0 to $ 2\pi $. Use different line styles, markers, and colors to distinguish between the two functions. Add a legend.


x = np.linspace(0, 2*math.pi, 30)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, marker='o', color='black', linestyle=':', label='sin(x)')
plt.plot(x, y2, marker='s', color='g', linestyle='--', label='cos(x)')

plt.xlabel('X values (radians)')
plt.ylabel('Function values')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.grid(True)
plt.show()


# ---

# #### **3. Subplots**
# - **Task**: Create a 2x2 grid of subplots. In each subplot, plot:
#   - Top-left: $ f(x) = x^3 $
#   - Top-right: $ f(x) = \sin(x) $
#   - Bottom-left: $ f(x) = e^x $
#   - Bottom-right: $ f(x) = \log(x+1) $ (for $ x \geq 0 $)

#   Customize each plot with titles, axis labels, and different colors.

fig, axis = plt.subplots(2, 2, figsize=(8, 6))

x = np.linspace(0, 10, 100)

y1 = x ** 3
y2 = np.sin(x)
y3 = np.exp(x)
y4 = np.log(x + 1)


# Top-left: x^3
axis[0, 0].plot(x, y1, color='purple')
axis[0, 0].set_title('f(x) = x³')
axis[0, 0].set_xlabel('x')
axis[0, 0].set_ylabel('y')
axis[0, 0].grid(True)

# Top-right: sin(x)
axis[0, 1].plot(x, y2, color='blue')
axis[0, 1].set_title('f(x) = sin(x)')
axis[0, 1].set_xlabel('x')
axis[0, 1].set_ylabel('y')
axis[0, 1].grid(True)

# Bottom-left: e^x
axis[1, 0].plot(x, y3, color='red')
axis[1, 0].set_title('f(x) = e^x')
axis[1, 0].set_xlabel('x')
axis[1, 0].set_ylabel('y')
axis[1, 0].grid(True)

# Bottom-right: log(x+1)
axis[1, 1].plot(x, y4, color='#238927')
axis[1, 1].set_title('f(x) = log(x+1)')
axis[1, 1].set_xlabel('x')
axis[1, 1].set_ylabel('y')
axis[1, 1].grid(True)


plt.tight_layout()
plt.show()


# ---

# #### **4. Scatter Plot**
# - **Task**: Create a scatter plot of 100 random points in a 2D space. The x and y values should be randomly generated from a uniform distribution between 0 and 10. Use different colors and markers for the points. Add a title, axis labels, and a grid.

x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.figure(figsize=(10, 6))  # set size before plotting
plt.scatter(x, y, c=y, cmap='viridis', edgecolors='black', marker='o')
plt.colorbar(label='Y value')
plt.grid(True)
plt.title('Scatter Plot of 100 Random Points (0-10)')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()


# ---

# #### **5. Histogram**
# - **Task**: Generate a random dataset of 1000 values sampled from a normal distribution (mean=0, std=1). Plot a histogram of the data with 30 bins. Add a title and axis labels. Adjust the transparency of the bars using the `alpha` parameter.

x = np.random.normal(loc=0, scale=1, size=1000)
plt.hist(x, bins=30, alpha=0.7, color='g', edgecolor='black')
plt.title('Histogram of 1000 Normally Distributed Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)
plt.show()

# ---

# #### **6. 3D Plotting**
# - **Task**: Create a 3D surface plot for the function $ f(x, y) = \cos(x^2 + y^2) $ over the range of $ x $ and $ y $ values from -5 to 5. Use a suitable colormap and add a colorbar. Set appropriate labels for the axes and title.

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)
X, Y = np.meshgrid(x, y)

Z = np.cos(X**2 + Y**2)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none') # type: ignore

fig.colorbar(surf, ax=ax, shrink=0.5, aspect=8)

ax.set_title('3D Surface Plot of f(x, y) = cos(x² + y²)')
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.show()

# ---

# #### **7. Bar Chart**
# - **Task**: Create a vertical bar chart displaying the sales data for five different products: `['Product A', 'Product B', 'Product C', 'Product D', 'Product E']`. The sales values for each product are `[200, 150, 250, 175, 225]`. Customize the chart with a title, axis labels, and different bar colors.

categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = [200, 150, 250, 175, 225]
colors = ['red', 'green', 'blue', 'orange', 'purple']  # one color per bar

plt.bar(categories, values, color=colors)
plt.title('Sales Data for Five Products')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.show()

# ---

# #### **8. Stacked Bar Chart**
# - **Task**: Create a stacked bar chart that shows the contribution of three different categories (`'Category A'`, `'Category B'`, and `'Category C'`) over four time periods (`'T1'`, `'T2'`, `'T3'`, `'T4'`). Use sample data for each category at each time period. Customize the chart with a title, axis labels, and a legend.


time_periods = ['T1', 'T2', 'T3', 'T4']

# Data for each category
cat_a = [20, 35, 30, 35]
cat_b = [25, 32, 34, 20]
cat_c = [15, 20, 25, 30]

# Plot
plt.bar(time_periods, cat_a, label='Category A', color='skyblue')
plt.bar(time_periods, cat_b, bottom=cat_a, label='Category B', color='orange')
plt.bar(time_periods, cat_c, bottom=np.array(cat_a) + np.array(cat_b), label='Category C', color='green')

# Labels & title
plt.title('Stacked Bar Chart: Category Contributions Over Time')
plt.xlabel('Time Periods')
plt.ylabel('Values')
plt.legend()

plt.show()
