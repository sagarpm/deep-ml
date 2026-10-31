def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

	r = len(a)
	c = len(a[0])

	v = len(b)
	if(c != v):
		return -1
	else:
		answer = []
		for i in range(r):
			summation = 0
			for j in range(c):
				summation += a[i][j]*b[j]
			
			answer.append(summation)
	
	return answer