import csv
import pandas as pd 
cnt = 0
dic = {}
data = pd.read_csv('full_music_data.csv')
print(data.head())
print(data.shape)