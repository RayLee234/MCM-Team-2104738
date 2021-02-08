import csv
import pandas as pd
import numpy as np
import math

df = pd.DataFrame(list())
df.to_csv('characteristic_contagiousness.csv')

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
# print(m)

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

numFollowers = [0] * n
adjacency_list = [0] * n

with open('influence_data.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		try:
			influencer = id2index[int(row[0])]
			follower = id2index[int(row[4])]
			numFollowers[influencer] += 1
			if adjacency_list[influencer] == 0:
				adjacency_list[influencer] = [follower]
			else:
				adjacency_list[influencer].append(follower)
		except:
			pass

numEdges = 0
for i in numFollowers:
	numEdges += i

print(m)

avg12 = [0] * n
with open('group_by_artist.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		try:
			if ', ' in row[0]:
				continue
			ID = int(row[0][1:-1])
			avg12[id2index[ID]] = row[2:14]
		except:
			pass

for i in range(n):
	if avg12[i] == 0:
		continue
	for j in range(12):
		avg12[i][j] = float(avg12[i][j])

# for row in avg12:
# 	if row == 0:
# 		continue
# 	print(len(row))

above = [0] * 12
below = [0] * 12
print(len(avg12), n)
# for i in avg12:
# 	print(i)
s = 0
t = n * (n-1) / 2
for i in range(n):
	print(i)
	for j in range(i+1,n):
		if avg12[i] == 0 or avg12[j] == 0:
			continue
		for k in range(12):
			if (not adjacency_list[i] == 0 and j in adjacency_list[i]) or (not adjacency_list[j] == 0 and i in adjacency_list[j]):
				below[k] += abs(avg12[i][k] - avg12[j][k])
				s += 1
			# print(avg12[i][k], avg12[j][k])
			above[k] += abs(avg12[i][k] - avg12[j][k])

s /= 12
print("---HERE---")
contag = [0] * 12
for i in range(12):
	contag[i] = (above[i] / t) / (below[i] / s)
	print(contag[i])

with open('characteristic_contagiousness.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow([])
	for i in range(n):
		writer.writerow(contag)