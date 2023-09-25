visited = set()
def dfs(node, movements):
    if node not in visited:
        visited.add(node)
        for neighbor in my_dict[node]:
            if neighbor not in visited:
                movements += 1
                movements = dfs(neighbor, movements)
    return movements

#The first input line contains an integer T (T < 100) that represents the number of test cases.
#Each test case begin with a line containing an integer N ( N < X2, where X is the size of the maze that can be from 3 up to 7). 
#This N is the node where the drawing must start and also finish. In the next input line there are two informations V and A that respectively represents the amount of vertices and edges of the maze. 
#Follow A lines, each one indicating a line segment that Peter must plot to draw the desired maze.

my_dict = {}
T = int(input()) # T = number of test cases
for _ in range(T):
    N = input() # N = node where the drawing must start and also finish
    V, A = input().split() # V = amount of vertices(nodes), A = edges(conexções) of the maze
    my_dict.clear()
    A = int(A)

    for j in range(A):
        node1, node2 = input().split()
        
        if my_dict.get(node1) is None:
            my_dict[node1] = [node2]
        else:
            if node2 not in my_dict[node1]:
                my_dict[node1].append(node2)

        if my_dict.get(node2) is None:
            my_dict[node2] = [node1]
        else:
            if node1 not in my_dict[node2]:
                my_dict[node2].append(node1)
    
    movements = 0
    visited.clear()
    movements = dfs(N, 0)
    print(movements*2)
    # for key, value in my_dict.items():
    #     print(key, ":", value)