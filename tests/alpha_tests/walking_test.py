import numpy as np

from model.agent.Agent import Agent
from model.direction_map.DirectionMap import DirectionMap
from model.environment.environment import direction_map
from model.environment.line import Point

star_pos = (1, 1)
end_pos = (99, 99)

collisions = np.zeros((100, 100)).tolist()

directions = direction_map(collisions, [Point(67, 70)], 3)

direct = DirectionMap(directions)

human_0 = Agent(star_pos, end_pos,3 , 3, 2, direct, collisions)
human_0.move()
human_0.move()
human_0.move()
human_0.move()
human_0.move()
human_0.move()
human_0.move()
human_0.move()
