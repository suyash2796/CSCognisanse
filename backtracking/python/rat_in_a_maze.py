#To solve Rat in a maze problem using backtracking

#initializing the size of the maze and soution matrix
N = 4 
solution_maze = [ [ 0 for j in range(N) ] for i in range(N) ]

def is_safe(maze, x, y ):
	'''A utility function to check if x, y is valid 
		return true if it is valid move,
		return false otherwise
	'''	
	if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1: 
		return True
	
	return False

def check_if_solution_exists(maze):
      
    if solve_maze(maze) == False: 
        print("Solution doesn't exist"); 
        return False
	
# recursive function to solve rat in a maze problem
def solve_maze(maze, x=0,y=0):
	'''
	This function will make several recursive calls
	until we reach to some finding, if we reach to destination
	following asafe path, then it prints the solution and return true,
	will return false otherwise.
	'''
	
	# if (x, y is goal) return True 
	if x == N - 1 and y == N - 1: 
		solution_maze[x][y] = 1
		print("solution:", solution_maze)
		return True
		
	# check if the move is valid
	if is_safe(maze, x, y) == True: 
		# mark x, y as part of solution path 
		# for(0,0) it sets up 1 in solution maze
		solution_maze[x][y] = 1
		
		# Move forward in x direction (recursive call)
		if solve_maze(maze, x + 1, y) == True:
			return True

		# Move down in y direction if moving in x direction is not fruitful
		#(recursive call)
		if solve_maze(maze, x, y + 1) == True: 
			return True
		
		#no option for rat to move, backtrack
		solution_maze[x][y] = 0
		return False

# Driver program to test above function 
if __name__ == "__main__": 
	maze = [ [1, 0, 0, 0], 
		[1, 1, 0, 1], 
		[1, 0, 0, 0], 
		[1, 1, 1, 1] ] 
			
	check_if_solution_exists(maze)

