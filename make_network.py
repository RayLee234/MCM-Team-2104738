import networkx as nx
from matplotlib import pyplot as plt
import random
from collections import deque
from colour import Color
import csv
G = nx.DiGraph()

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

num = 0
with open('influence_data.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		try:
			# if num > 30:
			# 	continue
			influencer = id2index[int(row[0])]
			follower = id2index[int(row[4])]
			print(influencer, follower)
			numFollowers[influencer] += 1
			G.add_edge(id2artist[index2id[follower]], id2artist[index2id[influencer]])
			num += 1
			if adjacency_list[influencer] == 0:
				adjacency_list[influencer] = [follower]
			else:
				adjacency_list[influencer].append(follower)
		except:
			pass

print(num)
nodes = list(G.nodes)
print(m)
print(nodes)
# maxIndex = 0
# for i in range(n):
# 	if numFollowers[i] > numFollowers[maxIndex]:
# 		maxIndex = i

# p = 3
# l = 3
# chosen = [0] * n
# chosen[maxIndex] = 1
# cnt = 1
# q = deque()
# q.append(maxIndex)

# for i in range(l-1):
# 	newChosen = []
# 	while len(q) > 0:
# 		x = q.popleft()
# 		if adjacency_list[x] != 0:
# 			idx = random.sample(range(len(adjacency_list[x])), min(len(adjacency_list[x]), p))
# 			for j in idx:
# 				if chosen[adjacency_list[x][j]] == 0:
# 					cnt += 1
# 					chosen[adjacency_list[x][j]] = 1
# 					newChosen.append(adjacency_list[x][j])
# 	for y in newChosen:
# 		q.append(y)

# print(cnt)

# numFollowers = [0] * n

# with open('influence_data.csv') as file:
# 	reader = csv.reader(file)
# 	for row in reader:
# 		try:
# 			influencer = id2index[int(row[0])]
# 			follower = id2index[int(row[4])]
# 			numFollowers[influencer] += 1
# 			if chosen[influencer] == 1 and chosen[follower] == 1:
# 				G.add_edge(id2artist[index2id[follower]], id2artist[index2id[influencer]])
# 		except:
# 			pass

# for 
# nx.spring_layout(G)
colors = ["red", "black", "blue", "yellow", "green", "orange", "pink", "purple", "tan", "magenta", "skyblue", "brown", "grey", "darkblue", "aqua", "violet", "gray", "darkgreen", "gold", "darkred"]
realColors = []
for node in nodes:
	try:
		realColors.append(colors[artist2genre[node]])
	except:
		realColors.append(colors[19])
print(realColors)
nx.spring_layout(G)
nx.draw(G, with_labels=False, node_color=realColors, node_size = 10, width = 0.05)
plt.show()