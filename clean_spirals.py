










from pprint import pprint as pp


class Spiral():


	def __init__(self, col,row, list_):
		self.col = col
		self.row = row
		self.one_dim = list_
		self.two_dim = self.create_spiral_matrix()


	def create_spiral_matrix(self):

		#return [['-' for col in range(self.col)] for row in range(self.row)]

		matrix_tmp = []
		for row in range(self.row):
			matrix_tmp.append(['-' for col in range(self.col)])

		return matrix_tmp		


	def print_spiral(self):
		for row in self.two_dim:
			print(row)	



	def spiralize(self):	


		one_dimension_pos = 0

		# populate first row
		first_row = self.one_dim[:self.row]
		self.two_dim[0] = first_row
		one_dimension_pos += self.row


		# populate last column
		for row_idx in range(1, self.col):
			self.two_dim[row_idx][-1] = self.one_dim[one_dimension_pos]
			one_dimension_pos += 1

		# populate last row 
		# 3 x 3 matrix
		# range(1, -1, -1 )
		for col_idx in range(self.col - 2, -1, -1):
			self.two_dim[-1][col_idx] = self.one_dim[one_dimension_pos]
			one_dimension_pos += 1


		# go upwards  
		for row_idx in range(self.row - 2, 0, -1):
			self.two_dim[row_idx][0] = self.one_dim[one_dimension_pos]
			one_dimension_pos += 1

		# go to the right
		for col_idx in range(1, self.col - 1):
			self.two_dim[row_idx][col_idx] = self.one_dim[one_dimension_pos]






def clean(ch):
	syms = [',', '[', ']', "'"]
	for sym in syms:
		ch = ch.replace(sym, '')
	return ch.strip()

def final(y):
    lis = y.split()
    digits_ = []
    for ch in lis:
        ch = clean(ch)
        if ch.isdigit():
            digits_.append(int(ch))
    digits_.sort()
    return digits_






if __name__ == '__main__':
    a = [[1, 2,  3,  4,  5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9]]

    list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    y = str(a)
    sp = Spiral(3,3, [1,2,3,4,5,6,7,8,9])
    sp.spiralize()
    sp.print_spiral()
    print(final(y))