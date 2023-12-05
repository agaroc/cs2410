import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

ballDf = pd.read_csv('all_seasons.csv')

def getSeasonAvrg(x, y):
    seasonAverages = {}
    for i in range(len(ballDf.index)):
        current = ballDf.loc[i, x]
        currentStr = current.split('-')[1]
        height = ballDf.loc[i, y]  
        if currentStr in seasonAverages:
            seasonAverages[currentStr].append(height)
        else:
            seasonAverages[currentStr] = [height]
    return seasonAverages

def exponential_func(x, a, b):
    return a * np.exp(b * x)

seasonAverages = getSeasonAvrg('season', 'player_height')  

seasonAverageHeight = []
for key in seasonAverages:
    total_height = sum(seasonAverages[key])
    num_players = len(seasonAverages[key])
    seasonAverageHeight.append(total_height / num_players)

seasons = ['97', '98', '99', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
plt.scatter(seasons, seasonAverageHeight)

params, covariance = curve_fit(exponential_func, range(len(seasons)), seasonAverageHeight)
a, b = params
growth_rate = np.exp(b) - 1
x_fit = np.arange(0, len(seasons), 0.1)
y_fit = exponential_func(x_fit, a, b)
plt.plot(x_fit, y_fit, 'r--', label=f'Exponential Fit (Growth Rate: {growth_rate:.2%})')

plt.xlabel('Season')
plt.ylabel('Average player height')
plt.title('Season vs Average player height')
plt.legend()
plt.show()
