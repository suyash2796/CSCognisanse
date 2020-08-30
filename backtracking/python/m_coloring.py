
# python program to solve m-coloring problem using backtracking 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 
  
    # This function checks if it is safe to color a vertex v with color c
    def isSafe(self, v, colour, c): 
        for i in range(self.V): 
            if self.graph[v][i] == 1 and colour[i] == c: 
                return False
        return True
      
    # A recursive function to solve m coloring problem
    def graphColourUtil(self, m, colour, v): 
        if v == self.V: 
            return True
  
        for c in range(1, m + 1): 
            if self.isSafe(v, colour, c) == True: 
                colour[v] = c 
                if self.graphColourUtil(m, colour, v + 1) == True: 
                    return True
                colour[v] = 0
  
    def graphColouring(self, m): 
        colour = [0] * self.V 
        if self.graphColourUtil(m, colour, 0) == None: 
            return False
        self.print_solution(colour)

    def print_solution(self, colour):
        # Print the solution 
        print("Solution exist")
        print("assigned colors are:")
        for c in colour: 
            print (c, end='')
        return True
  
# Driver program to test above function 
if __name__ == "__main__": 
    g = Graph(4) 
    g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]] 
    m = 3
    g.graphColouring(m) 
