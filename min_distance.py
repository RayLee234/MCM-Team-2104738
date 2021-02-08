import csv
from collections import deque

artist2id = {}
id2index = {}
index2id = {}
id2artist = {}

n = 0
with open('data_by_artist.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		# print(row)
		try:
			artist2id[row[0]] = int(row[1])
			id2artist[int(row[1])] = row[0]
			id2index[int(row[1])] = n
			index2id[n] = int(row[1])
			n += 1
		except:
			pass

# print(artist2id)
adjacency_matrix = [ 0 ] * n
num = 0
BR = []
JJ = []
CS = []
SB = []
TV = []
with open('influence_data.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		num += 1
		try:
			# print(num)
			influencer = id2index[int(row[0])]
			follower = id2index[int(row[4])]
			if id2artist[index2id[follower]] == "Jack Johnson":
				JJ.append(id2artist[index2id[influencer]])
			if id2artist[index2id[follower]] == "Bonnie Raitt":
				BR.append(id2artist[index2id[influencer]])
			if id2artist[index2id[follower]] == "Chris Smither":
				CS.append(id2artist[index2id[influencer]])
			if id2artist[index2id[follower]] == "Sam Bush":
				SB.append(id2artist[index2id[influencer]])
			if id2artist[index2id[follower]] == "Tom Verlaine":
				TV.append(id2artist[index2id[influencer]])
			# print(influencer, follower)
			# if adjacency_matrix[influencer] == 0:
			# 	adjacency_matrix[influencer] = [follower]
			# else:
			# 	adjacency_matrix[influencer].append(follower)
			# if adjacency_matrix[follower] == 0:
			# 	adjacency_matrix[follower] = [influencer]
			# else:
			# 	adjacency_matrix[follower].append(influencer)
			# if id2artist[index2id[follower]] == "Jack Johnson":
			# 	print(adjacency_matrix[id2index[artist2id["Jack Johnson"]]])
		except :
			pass

# print(adjacency_matrix)

min_distance_by_artist = [0] * n
print(len(BR))
print(len(JJ))
print(len(CS))
print(len(SB))
print(len(TV))

for i in range(n):
	if adjacency_matrix[i] != 0 and len(adjacency_matrix[i]) == 10:
		# print(id2artist[index2id[i]])
		if id2artist[index2id[i]] == "Jerry Garcia":
			for ID in adjacency_matrix[i]:
				print(id2artist[index2id[ID]])


# BFS
for i in range(n):
	q = deque()
	q.append(i)
	v = [0] * n
	d = [100000] * n
	v[i] = 1
	d[i] = 0
	while len(q) > 0:
		x = q.popleft()
		if(adjacency_matrix[x] == 0):
			continue
		for y in adjacency_matrix[x]:
			if v[y] < 1:
				v[y] = 1
				d[y] = d[x] + 1
				q.append(y)
	min_distance_by_artist[i] = d

# print(min_distance_by_artist)
