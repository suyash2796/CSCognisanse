#5x5 graph
input_graph = [[0, 1, 0, 1, 0],
   	[1, 0, 1, 0, 1],
   	[0, 1, 0, 0, 0],
   	[1, 1, 0, 0, 1],
   	[0, 1, 1, 1, 0]]


solution = [[0, 0, 0, 0, 0],
   	[0, 0, 0, 0, 0],
   	[0, 0, 0, 0, 0],
   	[1, 0, 0, 0, 0],
   	[0, 0, 0, 0, 0]]


def is_valid(v, pos, path):
	if input_graph[path[pos-1]][v]==0:
		return False
	for i in path:
		if i==v:
			return False
	
	return True

def ham_cycle():
	path= [-1,-1,-1,-1,-1]
	path[0]= 0

	if ham_cycle_track(path, 1)==False:
		print("No solution found")
		return False
	
	print(path)
	
	return True

def ham_cycle_track(path, pos):
	if pos ==5:
		if input_graph[path[pos-1]][path[0]] ==1:
			return True
		else:
			return False

	
	for v in range(1,5):
		if is_valid(v,pos,path) == True:
			path[pos] = v
			if ham_cycle_track(path, pos+1)==True:
				return True
			path[pos] = -1
	return False

ham_cycle()
