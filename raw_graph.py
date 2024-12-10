# Necessary libraies
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Figure settings
plt.figure(figsize=(12, 6))
mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False

# Load dataframe
df = pd.read_csv('data/Location1.csv')

# Clean datatimes 
date_time = pd.to_datetime(df.pop('Time'))
timestamp_s = date_time.map(pd.Timestamp.timestamp)

# Set index for every column
indexes = {name: i for i, name in enumerate(df.columns)}
n = len(df)

# Statistics values
train_df = df[0:int(n*0.70)]
val_df   = df[int(n*0.70):int(n*0.90)]
test_df  = df[int(n*0.90):]
num_features = df.shape[1]
train_mean = train_df.mean()
train_std = train_df.std()
train_df = (train_df-train_mean)/train_std
val_df = (val_df-train_mean)/train_std
test_df = (test_df-train_mean)/train_std
df_std = (df-train_mean)/train_std
df_std = df_std.melt(var_name='Columna', value_name='Valor Normalizado')
# Set the figure
ax = sns.violinplot(x='Columna', y='Valor Normalizado', data= df_std)
_ = ax.set_xticklabels(df.keys(), rotation=45)
plt.show()
