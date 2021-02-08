import csv
import pandas as pd

df = pd.DataFrame(list())
df.to_csv('music_data_by_genre.csv')

artist2id = {}
id2artist = {}
id2index = {}
index2id = {}

n = 0
with open('data_by_artist.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		try:
			artist2id[row[0]] = int(row[1])
			id2artist[int(row[1])] = row[0]
			id2index[int(row[1])] = n
			index2id[n] = int(row[1])
			n += 1
		except:
			pass

with open()