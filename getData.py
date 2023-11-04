import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ballDf = pd.read_csv('all_seasons.csv')
seasonAverages = {
}

def getSeasonAvrg():
    for i in range(len(ballDf.index)):
        current = ballDf.loc[i, 'season']
        currentStr = current.split('-')[1]
        points = ballDf.loc[i, 'pts']
        if currentStr in seasonAverages:
            seasonAverages[currentStr].append(points)
        else:
            seasonAverages[currentStr] = [points]
       # seasonAverages[current] = seasonAverages[current].append(ballDf.loc[i, 'pts'])



getSeasonAvrg()

seasonAveragePoints = []
for key in seasonAverages:
    x =0
    n=0
    for value in seasonAverages[key]:
        x += value
        n+=1
    seasonAveragePoints.append(x/n)
seasons = ['97', '98', '99', '00', '01', '02', '03', '04', '05', '06', '07', '08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
plt.scatter(seasons, seasonAveragePoints)
plt.xlabel('Season')
plt.ylabel('Average points per player')
plt.title('Season vs Average points per player')
plt.show()
