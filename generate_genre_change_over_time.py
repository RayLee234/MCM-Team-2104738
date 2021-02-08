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
genres = [""]

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

properties = ["danceability", "energy", "valence", "tempo", "loudness", "mode", "key", "acousticness", "instrumentalness", "liveness", "speechiness", "explicit"]

print(genres)

for genre in range(m):
	genreTot = [0] * 300
	genreSum = [[0] * 300, [0] * 300, [0] * 300, [0] * 300, [0] * 300, [0] * 300, [0] * 300, [0] * 300, [0] * 300, [0] * 300, [0] * 300, [0] * 300]

	with open('full_music_data_transformed.csv') as file:
		reader = csv.reader(file)
		for row in reader:
			try:
				ID = int(row[0][1:-1])
				name = id2artist[ID]
				if not name in artist2genre:
					continue
				g = artist2genre[name]
				if g != genre:
					continue
				time = int(row[15])
				for i in range(12):
					genreSum[i][time - 1800] += float(row[i+1])
				genreTot[time - 1800] += 1
			except ValueError:
				pass

	for i in range(300):
		for j in range(12):
			if genreTot[i] > 0:
				genreSum[j][i] /= genreTot[i]

	years = list(range(1800, 2025))
	years.insert(0, "")

	open(str(genre) + '.csv', "x")

	with open(str(genre) + '.csv', 'w', newline="") as file:
		writer = csv.writer(file)
		writer.writerow(years)
		for i in range(12):
			newRow = genreSum[i][0:225]
			newRow.insert(0, properties[i])
			writer.writerow(newRow)
		
