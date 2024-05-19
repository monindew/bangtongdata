import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import statsmodels.api as sm

os.chdir("C:/Github/bangtong/bangtongdata/data_bangtong/12강")

df = pd.read_csv("train.csv")
df = df[["SalePrice", "LotArea"]]
# print(df.head())

# ax = sns.scatterplot(df, x="SalePrice", y="LotArea")
# ax.set(ylim=(0, 50000))
# plt.show()

model = LinearRegression()
model.fit(X=df[["LotArea"]], y=df["SalePrice"])
# print(model.coef_, model.intercept_)

# print(model.predict([[1000]]))
x = df["LotArea"]
y = df["SalePrice"]

x = sm.add_constant(x)

model = sm.OLS(y, x).fit()

print(model.summary())