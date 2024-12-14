import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/Location1.csv")
time_step = df.pop("Time")

plt.figure(figsize = (10,10))
sns.heatmap(df.corr(), annot = True, cmap="coolwarm")
plt.show()
