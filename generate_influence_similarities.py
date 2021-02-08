import csv
import pandas as pd
import numpy as np
import math

df = pd.DataFrame(list())
df.to_csv('follower_non_follower_similarities.csv')

artist2id = {}
id2index = {}
index2id = {}
id2artist = {}

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

follower = [0] * n
nonFollower = [0] * n

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

for row in avg12:
	print(row)

weights_char = np.array([0.122320949130967, 0.170383444334258, 0.260195733537278, 0.135980853352454, 0.105168735560390, 0.164396042696526, 0.0415542413881274])
weights_vocal = np.array([0.232638782057617, 0.245759683848118, 0.0877430508282383, 0.247226302753251, 0.186632180512775])
alpha = 0.126487603026590
beta = 0.415185612756683

def dist(i, j):
	A = np.array(avg12[i])
	B = np.array(avg12[j])
	D = A - B
	return math.sqrt(alpha * np.sum(np.multiply(np.multiply(D[0:7], D[0:7]), weights_char)) + beta * np.sum(np.multiply(np.multiply(D[7:12], D[7:12]), weights_vocal)))


# for row in avg12:
# 	print(row)
for i in range(n):
	print(i)
	for j in range(n):
		if i == j:
			continue
		if avg12[i] == 0 or avg12[j] == 0:
			continue
		distance = dist(i, j)
		if adjacency_list[i] == 0 or not j in adjacency_list[i]:
			nonFollower[i] += distance
		else:
			follower[i] += distance
		if adjacency_list[j] == 0 or not i in adjacency_list[j]:
			nonFollower[j] += distance
		else:
			follower[j] += distance

for i in range(n):
	if numFollowers[i] != 0:
		follower[i] /= numFollowers[i]
	if numFollowers[i] != n:
		nonFollower[i] /= (n - numFollowers[i])
	# print(follower[i], nonFollower[i])

with open('follower_non_follower_similarities.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for i in range(n):
		writer.writerow([follower[i], nonFollower[i]])