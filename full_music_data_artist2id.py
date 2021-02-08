import csv
import pandas as pd

df = pd.DataFrame(list())
df.to_csv('transformed_data_for_optim.csv')

artist2id = {}
id2artist = {}
id2index = {}
index2id = {}

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

print(n)

with open('full_music_data_transformed.csv') as file:
	with open('transformed_data_for_optim.csv', 'w', newline='') as file2:
		writer = csv.writer(file2)
		writer.writerow([])
		reader = csv.reader(file)
		for row in reader:
			try:
				# print(row[0][1:len(row[0])-1])
				artists = row[0][1:len(row[0])-1]
				artists = artists.split(", ")
				for artistid in artists:
					newRow = row[1:13]
					newRow.insert(0, id2index[int(artistid)])
					# print(newRow)
					writer.writerow(newRow)
			except:
				pass

print(n)