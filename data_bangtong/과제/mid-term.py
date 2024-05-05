import pandas as pd
import os

os.chdir("C:/Github/bangtong/bangtongdata/data_bangtong/과제")

df = pd.read_csv("Political_Party_Survey_Data.csv")


# 처음 5개의 행 출력
print(df.head())

# 결측치 수 확인
print(df.isnull().sum())

# 정당별 평균 지지도 계산
avg_party = df.groupby('정당')['지지도'].mean()
print(avg_party)