import csv
import numpy as np
import math

artist2id = {}
id2index = {}
index2id = {}
id2artist = {}
artist2pr = {}

minWorkRequired = 3
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

num = 0
with open('artists_pr.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		if row[0] in artist2id:
			num += 1
			artist2pr[row[0]] = float(row[1])

def pr(name):
	try:
		return artist2pr[name]
	except:
		return 0

revolutions = [[1963, 1969], [1976, 1982], [2012, 2018]]
for r in revolutions:
	s = r[0]
	e = r[1]
	s_avg = np.zeros(12)
	e_avg = np.zeros(12)
	s_num = 0
	e_num = 0
	influencers = []
	with open('full_music_data_transformed.csv') as file:
		reader = csv.reader(file)
		for row in reader:
			try:
				t = int(row[15])
				if t != s and t != e:
					continue
				val = row[1:13]
				for i in range(12):
					val[i] = float(val[i])
				if t == s:
					s_avg += np.array(val)
					s_num += 1
				else:
					e_avg += np.array(val)
					e_num += 1
			except ValueError:
				pass
	s_avg /= s_num
	e_avg /= e_num
	revDir = e_avg - s_avg
	artistDir = [0] * n
	artistNum = [0] * n
	with open('full_music_data_transformed.csv') as file:
		reader = csv.reader(file)
		for row in reader:
			try:
				t = int(row[15])
				if t < s or t > e:
					continue
				ID = int(row[0][1:-1])
				idx = id2index[ID]
				if artistDir[idx] == 0:
					artistDir[idx] = [0] * 12
				artistNum[idx] += 1
				val = row[1:13]
				for i in range(12):
					val[i] = float(val[i])
					artistDir[idx][i] += val[i]
			except ValueError:
				pass
	print(len(artistNum))
	for i in range(n):
		if artistNum[i] < minWorkRequired:
			artistDir[i] = 0
			continue
		for j in range(12):
			artistDir[i][j] /= artistNum[i]
			artistDir[i][j] -= s_avg[j]
		D = np.array(artistDir[i])
		Cos = np.dot(D, revDir) / np.linalg.norm(D) / np.linalg.norm(revDir)
		if Cos >= requiredDeg:
			influencers.append(id2artist[index2id[i]])
	print(s, e)
	influencers.sort(key=pr, reverse=True)
	print(influencers)
