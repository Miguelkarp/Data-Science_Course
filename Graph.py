import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/Location1.csv")
df_ax = df[["temperature_2m","relativehumidity_2m","dewpoint_2m","windspeed_10m","windspeed_100m","Power"]]

sns.regplot(x="Power", y = "windspeed_10m", data = df, scatter_kws = {'alpha': 0.5}, line_kws={'color':'red'})
sns.regplot(x="Power", y = "windspeed_100m", data = df, scatter_kws = {'alpha': 0.5}, line_kws={'color':'green'})
plt.title("windspeed vs Power")

plt.show()
            
fig, axes = plt.subplots(3,2, figsize = (12,12))
axes = axes.flatten()

for i, col in enumerate(df_ax.columns.tolist()):
    sns.histplot(df[col], kde = True, ax=axes[i])
    axes[i].set_title(f'Distribucion de {col}')
    
plt.show()

