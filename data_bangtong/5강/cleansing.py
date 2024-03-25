import pandas as pd
import os

os.chdir("C:/Github/bangtong/bangtongdata/data_bangtong/5강")

df = pd.read_csv("patient.csv")

print(df)

missing_values_cnt = df.isnull().sum()
print(missing_values_cnt)