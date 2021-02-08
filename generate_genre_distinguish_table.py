import csv
import pandas as pd
import numpy as np
import math


artist2id = {}
id2index = {}
index2id = {}
id2artist = {}

genre2id = {}
id2genre = {}
artist2genre = {}
genres = []

m = 0
with open('influence_data.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		try:
			x = int(row[0])
			if not row[2] in genre2id:
				genre2id[row[2]] = m
				id2genre[m] = row[2]
				genres.append(row[2])
				m += 1
			artist2genre[row[1]] = genre2id[row[2]]
			artist2genre[row[5]] = genre2id[row[6]]
		except:
			pass

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

properties = ["", "danceability", "energy", "valence", "tempo", "loudness", "mode", "key", "acousticness", "instrumentalness", "liveness", "speechiness", "explicit"]

genreNum = [0] * m
genreMean12 = [0] * m
with open('full_music_data_transformed.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		try:
			ID = int(row[0][1:-1])
			name = id2artist[ID]
			if not name in artist2genre:
				continue
			g = artist2genre[name]
			genreNum[g] += 1
			if genreMean12[g] == 0:
				genreMean12[g] = [0] * 12
			val = row[1:13]
			for i in range(12):
				val[i] = float(val[i])
				genreMean12[g][i] += val[i]
		except ValueError:
			pass

tot = sum(genreNum)
print(tot)

for gr in genreMean12:
	print(gr)

open('genre_distinguish_table_ratio.csv', "x")

with open('genre_distinguish_table_ratio.csv', 'w', newline="") as file:
	writer = csv.writer(file)
	writer.writerow(properties)
	for i in range(m):
		newRow = [0] * 12
		for c in range(12):
			fst = genreMean12[i][c] / genreNum[i]
			totNum = 0
			for j in range(m):
				if i != j:
					totNum += genreNum[j]
			snd = 0
			for j in range(m):
				if i != j:
					snd += genreMean12[j][c] / totNum
			newRow[c] = (fst - snd) / snd
		newRow.insert(0, genres[i])
		writer.writerow(newRow)
