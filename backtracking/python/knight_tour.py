# Solving knight tour problem using python 3

# input the Chessboard Size 
n = int(input("Enter the size of chessboard: "))

def checkifsafe(x,y,board): 
	'''check if the index is valid in a chessboard,
		also check if the index is not visited already'''
	if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1): 
		return True
	return False

def display_solution(n, board): 
	''' 
	A utility function to print solution 
	'''
	for i in range(n): 
		for j in range(n): 
			print(board[i][j],end =' ') 
		print() 


def solve_knight_tour(n): 
	''' 
	Knight gets on a tour, checks successive path if safe to travel,
	gets back on the previous path if unsafe. Prints the solution,
	if visit all blocks otherwise display that path doesn't exist
	'''
	
	# Initialization of Board matrix 
	board = [[-1 for i in range(n)]for i in range(n)] 
	
	# move_x and move_y define next move of Knight. 
	# move_x is for next value of x coordinate 
	# move_y is for next value of y coordinate 
	move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
	move_y = [1, 2, 2, 1, -1, -2, -2, -1] 
	
	# Since the Knight is initially at the first block 
	board[0][0] = 0
	
	# Step counter for knight's position 
	pos = 1
	
	# Checking if solution exists or not 
	if(not check_knight_tour(n, board, 0, 0, move_x, move_y, pos)): 
		print("Solution does not exist") 
	else: 
		display_solution(n, board) 

def check_knight_tour(n,board,curr_x,curr_y,move_x,move_y,pos): 
	''' 
		A recursive function to solve Knight Tour 
		problem 
	'''
	
	if(pos == n**2): 
		return True
	
	# check all next moves from current coordinate
	for i in range(8): 
		new_x = curr_x + move_x[i] 
		new_y = curr_y + move_y[i] 
		if(checkifsafe(new_x,new_y,board)): 
			board[new_x][new_y] = pos 
			if(check_knight_tour(n,board,new_x,new_y,move_x,move_y,pos+1)): 
				return True
			
			# Backtrack 
			board[new_x][new_y] = -1
	return False
		
# Driver program to test above function 
if __name__ == "__main__": 
	solve_knight_tour(n) 

