import csv
import matplotlib.pyplot as plt
import numpy as np
import math

year12 = [0] * 3000
yearNum = [0] * 3000
with open('full_music_data_transformed.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		try:
			t = int(row[15])
			yearNum[t] += 1
			if year12[t] == 0:
				year12[t] = [0] * 12
			val = row[1:13]
			for i in range(12):
				val[i] = float(val[i])
				year12[t][i] += val[i]
		except ValueError:
			pass

for i in range(3000):
	if yearNum[i] == 0:
		continue
	for j in range(12):
		year12[i][j] /= yearNum[i]
	print(year12[i])

weights_char = np.array([0.122320949130967, 0.170383444334258, 0.260195733537278, 0.135980853352454, 0.105168735560390, 0.164396042696526, 0.0415542413881274])
weights_vocal = np.array([0.232638782057617, 0.245759683848118, 0.0877430508282383, 0.247226302753251, 0.186632180512775])
alpha = 0.126487603026590
beta = 0.415185612756683

def dist(i, j):
	A = np.array(year12[i])
	B = np.array(year12[j])
	D = A - B
	return math.sqrt(alpha * np.sum(np.multiply(np.multiply(D[0:7], D[0:7]), weights_char)) + beta * np.sum(np.multiply(np.multiply(D[7:12], D[7:12]), weights_vocal)))

time = list(range(1958, 2020))
diff = []

n = 5
for t in time:
	diff.append(dist(t, t-3))

plt.plot(time, diff)
plt.show()
