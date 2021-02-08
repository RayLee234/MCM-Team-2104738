import csv
import numpy as np
import math

artist2id = {}
id2index = {}
index2id = {}
id2artist = {}
artist2pr = {}

# minWorkRequired = 3
requiredDeg = math.sqrt(2) / 2

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

genre2id = {}
id2genre = {}
artist2genre = {}
genres = []

genre = 6

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

# print(genres)
artistCareer = [0] * n
RB = []
with open('full_music_data_transformed.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		try:
			t = int(row[15])
			if t < 1960 or t > 2015:
				continue
			ID = int(row[0][1:-1])
			idx = id2index[ID]
			# print(artist2genre[id2artist[ID]])
			if artist2genre[id2artist[ID]] != genre:
				continue
			if not id2artist[ID] in RB:
				RB.append(id2artist[ID])
			if artistCareer[idx] == 0:
				artistCareer[idx] = []
			if not t in artistCareer[idx]:
				artistCareer[idx].append(t)
		except:
			pass

# print(len(RB))
# print(RB)
for i in range(n):
	if artistCareer[i] != 0:
		artistCareer[i] = len(artistCareer[i])
# print(artistCareer)
influenceYears = [0] * n
for year in range(1960, 2015):
	now = [0] * 12
	cntNow = 0
	future = [0] * 12
	cntFuture = 0
	a = [0] * n
	cntA = [0] * n
	all3 = [0] * 12
	cnt3 = 0
	with open('full_music_data_transformed.csv') as file:
		reader = csv.reader(file)
		for row in reader:
			try:
				t = int(row[15])
				ID = int(row[0][1:-1])
				if artist2genre[id2artist[ID]] != genre:
					continue
				if t == year:
					cntNow += 1
					val = row[1:13]
					for i in range(12):
						val[i] = float(val[i])
						now[i] += val[i]
				elif t == year + 5:
					cntFuture += 1
					val = row[1:13]
					for i in range(12):
						val[i] = float(val[i])
						future[i] += val[i]
				if t >= year and t < year + 3:
					val = row[1:13]
					for i in range(12):
						val[i] = float(val[i])
					ID = int(row[0][1:-1])
					idx = id2index[ID]
					if a[idx] == 0:
						a[idx] = [0] * 12
					cntA[idx] += 1
					cnt3 += 1
					for i in range(12):
						a[idx][i] += val[i]
						all3[i] += val[i]
			except:
				pass
	dirRB = [0] * 12
	for i in range(12):
		dirRB[i] = future[i] / cntFuture - now[i] / cntNow
	for artist in RB:
		idx = id2index[artist2id[artist]]
		mu = [0] * 12
		if a[idx] == 0:
			continue
		for i in range(12):
			mu[i] = all3[i] - a[idx][i]
		dirThis = [0] * 12
		for i in range(12):
			dirThis[i] = a[idx][i] / cntA[idx] - mu[i] / (cnt3 - cntA[idx])
		A = np.array(dirRB)
		B = np.array(dirThis)
		Cos = np.dot(A, B) / np.linalg.norm(A) / np.linalg.norm(B)
		if Cos >= requiredDeg:
			influenceYears[idx] += 1

percent = .3

idx = id2index[artist2id["Michael Jackson"]]
print("Proportion of MJ: ", influenceYears[idx], artistCareer[idx])

dynamic_influencers = []
for artist in RB:
	idx = id2index[artist2id[artist]]
	if artistCareer[idx] == 0:
		continue
	if influenceYears[idx] >= artistCareer[idx] * percent and artistCareer[idx] >= 10:
		print(influenceYears[idx], artistCareer[idx])
		dynamic_influencers.append(artist)

print(dynamic_influencers)
for artist in dynamic_influencers:
	print(influenceYears[id2index[artist2id[artist]]], artistCareer[id2index[artist2id[artist]]], influenceYears[id2index[artist2id[artist]]]/artistCareer[id2index[artist2id[artist]]])

# def numYears(name):
# 	return influenceYears[id2index[artist2id[name]]]

# RB.sort(key=numYears, reverse=True)
# print(RB)