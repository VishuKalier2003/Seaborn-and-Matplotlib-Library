import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
from urllib.request import urlretrieve

# Line Chart (simplest and most widely used)
a = [0.85, 0.9, 0.11, 0.45, 0.55, 0.80, 0.23, 0.81]      # A set of values
b = [1, 2, 3, 4, 5, 6, 7, 8]                         # Another set of values
plt.plot(b, a)     # First value is for the x-axis and second for the y-axis
plt.show()      # Showing the plotted graph

# Customizing the Axes and the Labels
yr = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
val = [6, 4, 10, 2, 4, 8, 12]
plt.xlabel('Years')              # X-label
plt.ylabel('Values')             # Y-label
plt.plot(yr, val)    # Years on x-axis and values on y-axis
plt.show()           # Showing the graph
b = [2, 8, 4, 10, 8, 4, 12]
# Various other styling properties are linewidth, linestyle, markersize, markeredgecolor, markeredgewidth, markerfacecolor, alpha, color, marker
plt.figure(figsize=(12, 7))     # perfect figure size
plt.plot(yr, val, marker='o', color='lightblue')           # Val and b values plotted in same graph
plt.plot(yr, b, marker='x', color='orange')    # Using marker and Color for the points in graph
plt.title("Line Graph")      # Plot title
plt.legend(['Values1', 'Values2'])    # Putting the legends in the plot for user to visualize
plt.show()       # Showing the graph

# Seaborn Library is advanced Matplotlib Library for better customization to the end users
sn.set_style('whitegrid')      # Applying the pre defined styles of seaborn library globally
plt.plot(yr, val, marker='o', color='lightblue', ls='--', lw='1', alpha=0.8, markerfacecolor='blue')
plt.plot(yr, b, marker='o', color='orange', ls='dotted', lw='1', alpha=0.6, markerfacecolor='red')
plt.show()      # Applying both the predefined styles and the user-defined styles in the graph
# Applying the pre defined styles of seaborn library globally
sn.set_style('darkgrid')
plt.plot(yr, val, marker='o', color='lightblue', ls='--', lw='1', alpha=0.8, markerfacecolor='blue')
plt.plot(yr, b, marker='o', color='orange', ls='dotted', lw='1', alpha=0.6, markerfacecolor='red')
plt.show()      # Applying both the predefined styles and the user-defined styles in the graph

# Scatter Plot plots the values of two or more variables as points in a 2d graph
a1 = np.random.randint(1, 20, size=40)   # Random values of size 40
b1 = np.random.randint(1, 30, size=40)   # Random values of size 40
sn.scatterplot(a1, b1, s=100) # size is 100
# Hue property is used when we have another array of length equal to the values array which can be used as a distinguishing property

# Histogram shows the distribution of data by forming bins or rectangular bars along the range of data showing visualization in numbers
plt.hist(b)    # Only one value needs to be passed
plt.hist(b, bins=5)    # The number of bins can be set here
plt.hist(b, bins=np.arange(1, 12, 0.5))   # The size of each bins set as 50% of its normal size
# Multiple histograms on same chart
plt.hist(a, bins=np.arange(1, 14, 0.5), alpha=0.5)  # alpha property used so that the bins dont mix up
plt.hist(b, bins=np.arange(1, 14, 0.5), alpha=0.5)
plt.show()
# Passing multiple values in the histogram as a list [a, b]
plt.hist([a, b], bins=np.arange(1, 15, 0.5), alpha=0.5) # alpha property used so that the bins dont mix up
plt.show()
plt.hist([a, b], bins=np.arange(1, 15, 0.5), alpha=0.5, stacked=True)  # To stack on one another

# Bar chart shows bar for each value instead of a line and is also most commonly used
plt.bar(yr, val)     # Plotting two values in a bar chart
plt.bar(yr, val, bottom=b)   # Stacking bars one above another
ax = plt.gca()
tip = sn.load_dataset('tips')      # Pre existing data frame
lines = ax.lines[0]
lines.get_xydata()
# The thick line over each bar tells the variation and is termed as the confidence interval
sn.barplot('day', 'total_bill', data=tip)        # Data to the barplot passed as the tip Dataframe
# The barplot method computes the averages automatically as well

# Heatmap is used to visualize 2d dat in the form of matrix or table marked all over with colors
flight = sn.load_dataset('flights')
flight = flight.pivot('month', 'year', 'passengers')     # We use pivot method to convert to 2d matrix
sn.heatmap(flight)     # Now that 2d matrix is visualized using heatmap
sn.heatmap(flight, annot=True)    # To show th actual values in every element of the matrix
sn.heatmap(flight, annot=True, fmt='d')     # fmt reduces the values to integer
sn.heatmap(flight, annot=True, fmt='d', cmap='Reds')    # Another color map

# Importing and Displaying Images using Seaborn and Matplotlib Library
urlretrieve('https://i.imgur.com/SkPbq.jpg', 'chart.jpg')
from PIL import Image     # Images Library
img = Image.open('chart.jpg')
# An image from PIL is a 3d numpy array containing intensities of Red, Green and Blue colors for every pixel in the image...
array = np.array(img)      # Converting the image to an array
print(array.shape)
plt.grid(False)     # No grid lines
plt.axis('off')    # No axes
plt.imshow(img)     # Displaying image using plt
plt.imshow(array[100:400, 105:300])       # Displaying a part of the image.. The slicing is done on the image array created and not on the image take from the net...

# Multiple charts in a grid...
fig, axes = plt.subplots(2, 3, figsize=(16, 8))   # 2, 3 mean 6 plots can be plotted in the grid of 2 row and 3 columns
axes[0][0].plot(yr, b)
axes[0][1].set_title('scatterplot')
sn.scatterplot(a1, b1, s=100, ax=axes[0][1])
sn.pairplot(a1, b1)       # Seaborn automatically creates different types of graphs using pairplot method... hue property can also be added...
sn.pairplot(tip, hue='sex')

# Distribution Graph
sn.displot(b)    # Bar chart with a line graph to interpret slope

# Contour Graph
iris = sn.load_dataset('iris')
sn.kdeplot(iris['sepal_length'], iris['sepal_width'], shade=True)   # Contour Plot with shades
sn.kdeplot(iris['sepal_length'], iris['sepal_width'], shade=True, shade_lowest=False)    # Shade the background...
sn.kdeplot(iris['sepal_length'], iris['sepal_width'], shade=False, shade_lowest=False)   # The area between the contour lines is not shaded...
setosa = iris[iris['species'] == 'setosa']         # Setosa petals array dataset
virginica = iris[iris['species'] == 'virginica']   # Virginica petal array dataset
sn.kdeplot(setosa['sepal_length'], setosa['sepal_width'], shade=True, shade_lowest=False)          # The contour plot of the setosa petals
sn.kdeplot(virginica['sepal_length'], virginica['sepal_width'], shade=True, shade_lowest=False)    # The contour plot of the virginica petals

# Box Graph
sn.boxplot(tip['day'], tip['total_bill'], hue=tip['smoker'])     # Show the nested BoxPlot by day and total bill hueing or differentiating between the smokers

# Another way to subplot
plt.subplot(1, 2, 1)    # A plot having 1 row and 2 column and subplot is located in 1st position
plt.plot(tip['day'], marker='o', color='orange', markerfacecolor='red', linestyle='solid')
plt.xlabel('Months')
plt.ylabel('Death Ratio')
plt.title("Monthly Covid Death Ratio")
plt.subplot(1, 2, 2)    # A plot having 1 row and 2 column and subplot is located at 2nd position
plt.plot(tip['total_bill'], marker='o', color='orange', markerfacecolor='red', linestyle='solid')
plt.xlabel('Years')
plt.ylabel('Death Ratio')
plt.title('Yearly Covid Death Ratio')
plt.show()      # Displaying the plot