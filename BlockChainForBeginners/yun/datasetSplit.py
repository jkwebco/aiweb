import pandas as pd

#loading our data as a panda
df = pd.read_csv('winequality-red.csv', delimiter=";")

#getting only the column called quality
label = df['quality']

#getting every column except for quality
features = df.drop('quality', axis=1)
