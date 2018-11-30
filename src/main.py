from environment.a_star import astar
from environment.environment import map_environment


def print_maze(maze):
    for j in range(0,len(maze)):
        for i in range(0,len(maze[j])):
            if maze[j][i] == 2:
                maze[j][i] = 0

    # maze[agent.start[0]][agent.start[1]] = 2
    # for i in range(0, len(maze[0])):
    #     print(maze[i])
    # print()


maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


#print(astar(maze, (0, 0), (9, 1)))

for ele in map_environment(maze, [(9, 1),(9,2)]):
    print(ele)







