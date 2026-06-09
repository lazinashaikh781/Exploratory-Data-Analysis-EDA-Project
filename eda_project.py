import pandas as pd

df = pd.read_csv("Titanic_Cleaned.csv")

print(df.describe())
print(df.info())

import seaborn as sns
import matplotlib.pyplot as plt

numeric_df = df.select_dtypes(include=['number'])

#plt.figure(figsize=(8,6))
#sns.heatmap(numeric_df.corr(), annot=True)
#plt.title("Correlation Heatmap")
#plt.show()


#plt.figure(figsize=(8,5))
#sns.histplot(df['Age'], bins=20)
#plt.title("Age Distribution")
#plt.show()
#sns.countplot(x='Sex', hue='Survived', data=df)
#plt.title("Gender vs Survival")
#plt.show()

#sns.countplot(x='Pclass', hue='Survived', data=df)
#plt.title("Passenger Class vs Survival")
#plt.show()

sns.boxplot(x=df['Fare'])
plt.title("Fare Distribution")
plt.show()