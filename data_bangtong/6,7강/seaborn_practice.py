import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


os.chdir("C:/Github/bangtong/bangtongdata/data_bangtong/6,7강")
df = pd.read_csv("recent-grads.csv")

sns.set_theme(context='notebook', style='darkgrid', palette='bright',
              font='Malgun Gothic', font_scale=1, rc={"axes.unicode_minus":False})
# f, ax = plt.subplots(figsize=(5,4))

df_tips = sns.load_dataset('tips')
# sns.barplot(x="day", y="total_bill", data=df_tips)
# sns.violinplot(x="day", y="tip", hue="sex", data=df_tips)

f, ax = plt.subplots(figsize=(8,4))
gs = f.add_gridspec(1,3)

ax = f.add_subplot(gs[0,0])
sns.boxplot(df["Median"])
ax = f.add_subplot(gs[0,1])
sns.boxenplot(df["Median"])
ax = f.add_subplot(gs[0,2])
sns.violinplot(df["Median"])
f.tight_layout()
plt.show()