import pandas as pd
df = pd.read_csv("D:\machine_learning\kelulusan_mahasiswa.csv")
print(df.info())
print(df.head())

print(df.isnull().sum())
df = df.drop_duplicates()

import seaborn as sns
sns.boxplot(x=df['IPK'])