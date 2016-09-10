import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import AutoMinorLocator



#Creating Dataframe
df = pd.read_csv("U_S_Pop_Data.csv", index_col = 0, usecols = (2,3,4,5), header = None, skiprows = (0,1,2), names = ["State","Both Sexes","Male","Female"] )
pd.set_option('display.width', 160)

#Initialzing the figure for customization, then changing the bg color to white
fig = plt.figure()
fig.patch.set_facecolor('white')

#Initializing the axes for customization
ax = plt.axes()
#Changing x-axis numbers from scientific notation to regular numbers
ax.get_xaxis().get_major_formatter().set_scientific(False)

#Adjusting the spacing of the states (most effective when enlarged)
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))

#setting the width of the bars for the graph
width = 0.35

#setting the populations to a variable
population = np.arange(len(df.index))

#Plotting both the Female & Male populations
plt.barh(population,df['Female'], width, color = "#fd77ab", label = "Female", zorder="3")
plt.barh(population + width + .01,df['Male'],width, color = "#1976D2", label = "Male", zorder="3")

#Creating a legend for the graph
ax.legend(ncol=1,prop={'size':12}).get_frame().set_alpha(0.4)

#Setting a title and a label for each axis
ax.set_title('50 States & Puerto Rican Population based on 2010 Census', fontsize=10)

#Changing the background of the axis
ax.set_axis_bgcolor('#f6f6f6')

#Adding/Editing minor grind lines
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
plt.grid(b=True, which='minor', color='grey', linestyle='-', alpha = 0.2)
ax.grid(zorder=0, color='black')

#Making sure Millions are shown as "1,000,000" & not "1000000"
ax.get_xaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

#Setting the increments for each axis
plt.xticks(np.arange(0, 20000000, 1000000), fontsize='9')
plt.yticks(np.arange(0, 52, 1))

#Setting the y axis tickers to a variable
labels = [item.get_text() for item in ax.get_yticklabels()]

#Adjusting the size of the y axis tick labels
ax.set_yticklabels(labels, fontsize='9')

#Rotating the x axis labels
for label in ax.xaxis.get_ticklabels():
		label.set_rotation(45)

#Getting the name of each state and setting it to it's corresponing population
states = []
for state in df.index:
    states.append(state)
ax.set_yticklabels(states)


plt.show()




