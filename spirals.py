class Spirals:

	def __init__(self, row_end, col_end, a):
		self.row_end = row_end
		self.col_end = col_end
		self.a = a
		self.row_start = 0
		self.col_start = 0


	def print_it(self):
		"""
		row_start => starting row index
		row_end => ending row index
		col_start => starting column index
		col_end => ending column index
		i => iterator
		"""

		while (self.row_start < self.row_end and self.col_start < self.col_end):
			for i in range(self.col_start, self.col_end):
				print(self.a[self.row_start][i], end=" ")
			self.row_start += 1

			for i in range(self.row_start, self.row_end):
				print(self.a[i][self.col_end - 1], end=" ")
			self.col_end -= 1

			if (self.row_start < self.row_end):

				for i in range(self.col_end - 1, (self.col_start - 1), -1):
					print(self.a[self.row_end - 1][i], end=" ")
				self.row_end -= 1

			if (self.col_start < self.col_end):
				for i in range(self.row_end - 1, self.row_start - 1, -1):
					print(self.a[i][self.col_start], end=" ")

				self.col_start += 1

	def despiral(self, matrix):
		res = []
		for i in matrix:
			for j in i:
				res.append(j)
		res.sort()
		
		return res
        

if __name__ == '__main__':
	

	a = [[1, 2,  3,  4,  5],
	    [16, 17, 18, 19, 6],
	    [15, 24, 25, 20, 7],
	    [14, 23, 22, 21, 8],
	    [13, 12, 11, 10, 9]]
		
	R = 5
	C = 5
	sp = Spirals(R, C, a)
	sp.print_it()
	print()
	print(sp.despiral(a))