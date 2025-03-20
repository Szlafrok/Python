T = [4, 2, 1, 5, 4, 7, 6, 9, 7, 8]
zliczenia = []
posortowana = []

for num in range(1, 10):
	x = 0
	if num in T:
		for i in range(len(T)):
			if T[i] == num:
				x += 1
	else:
		x = 0
	zliczenia.append(x)

for zliczenie in enumerate(zliczenia):
	print(zliczenie)
	if zliczenie[1] >= 1:
		for _ in range(zliczenie[1]):
			posortowana.append(zliczenie[0] + 1)

print(posortowana)

