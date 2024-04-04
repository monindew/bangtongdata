import pandas as pd
import os
import matplotlib.pyplot as plt

os.chdir("C:/Github/bangtong/bangtongdata/data_bangtong/6,7강")
df = pd.read_csv("recent-grads.csv")
print(df)

# plt.plot([0,1,2,3], [0,1,2,3], 'ro')
# plt.plot([1,2,3,4], [1,4,9,16], 'b-')
df.plot(x="Rank", y=["P25th", "Median", "P75th"])
plt.show()