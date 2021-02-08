import csv
import pandas as pd

df = pd.DataFrame(list())
df.to_csv('influence_table.csv')

genre2id = {}
id2genre = {}
genres = [""]

n = 0
with open('influence_data.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		try:
			x = int(row[0])
			print(row[2])
			if not row[2] in genre2id:
				genre2id[row[2]] = n
				id2genre[n] = row[2]
				genres.append(row[2])
				n += 1
		except:
			pass

print(genre2id)

table = [0] * n
for i in range(n):
	table[i] = [0] * n

with open('influence_data.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		try:
			x = int(row[0])
			influencerId = genre2id[row[2]]
			followerId = genre2id[row[6]]
			table[followerId][influencerId] += 1
		except:
			pass

s = [0] * n
for i in range(n):
	s[i] = sum(table[i])
for i in range(n):
	for j in range(n):
		table[i][j] /= s[i]

with open('influence_table.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(genres)
	for i in range(n):
		newRow = table[i][0:n]
		newRow.insert(0, id2genre[i])
		writer.writerow(newRow)