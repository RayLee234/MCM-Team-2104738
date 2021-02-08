import csv
import pandas as pd

df = pd.DataFrame(list())
df.to_csv('mean_for_each_genre.csv')

genre2id = {}
id2genre = {}
artist2genre = {}
genres = [""]

n = 0
with open('influence_data.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		try:
			x = int(row[0])
			if not row[2] in genre2id:
				genre2id[row[2]] = n
				id2genre[n] = row[2]
				genres.append(row[2])
				n += 1
			artist2genre[row[1]] = genre2id[row[2]]
			artist2genre[row[5]] = genre2id[row[6]]
		except:
			pass

# print(artist2genre)

artist2id = {}
id2artist = {}
id2index = {}
index2id = {}

m = 0
with open('data_by_artist.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		try:
			artist2id[row[0]] = int(row[1])
			id2artist[int(row[1])] = row[0]
			id2index[int(row[1])] = m
			index2id[m] = int(row[1])
			m += 1
		except:
			pass

genre_mean = [0] * n
genre_num = [0] * n
properties = [""]
for i in range(n):
	genre_mean[i] = [0] * 12
with open('full_music_data_transformed.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		try:
			artists = row[0][1:len(row[0])-1]
			artists = artists.split(", ")
			# print(artists)
			for artistId in artists:
				if not id2artist[int(artistId)] in artist2genre:
					continue
				g = artist2genre[id2artist[int(artistId)]]
				genre_num[g] += 1
				for j in range(12):
					genre_mean[g][j] += float(row[j+1])
		except:
			print(row)
			for j in range(1,13):
				properties.append(row[j])

print(properties)
print(n)
for i in range(n):
	for j in range(12):
		genre_mean[i][j] /= genre_num[i]

print(genre_mean)

with open('mean_for_each_genre.csv', 'w', newline="") as file:
	writer= csv.writer(file)
	writer.writerow(properties)
	for i in range(n):
		newRow = genre_mean[i][0:12]
		newRow.insert(0, id2genre[i])
		# print(newRow)
		writer.writerow(newRow)
