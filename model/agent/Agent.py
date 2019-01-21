import random

import numpy as np

import model.navigator.navigator as nav
from model.direction_map import DirectionMap
from model.collisions.collision_map_tools import mark_location
from model.environment.environment_enum import Env


class Agent:
    def __init__(self, start_position: (int, int), end_position: [(int, int)], directions_map: [DirectionMap],
                 collision_map: [[(int, int)]], bound_size=2, max_step=1,mode=0 ):

        self.start = start_position
        self.end = end_position
        self.current_pos = self.start
        self.max_step = max_step
        self.front_collision_size = bound_size
        self.direction_map = directions_map[mode]
        self.collision_map = collision_map
        self.facing_angle = self.direction_map.get_angle(self.current_pos)

        self.forward_move_angle = np.pi * (9 / 10)
        self.minimal_move_price = 0.05
        self.anger = 0;
        self.block_space()

    def update_facing_angle(self, nex_move):
        if nex_move == self.current_pos:
            self.facing_angle = self.direction_map.get_angle(self.current_pos)
        else:
            self.facing_angle = nav.get_angle_of_direction_between_points(self.current_pos, nex_move)

    def get_possible_moves(self):
        available_points = []
        (a_y, a_x) = self.current_pos

        for x in range(a_x - self.max_step, a_x + self.max_step + 1):
            for y in range(a_y - self.max_step, a_y + self.max_step + 1):

                if y >= len(self.collision_map) or x >= len(self.collision_map[y]):
                    continue
                if self.collision_map[y][x] == 0:

                    distance = nav.get_distance_beteween_points(self.current_pos, (y, x))
                    angle = nav.get_angle_of_direction_between_points(self.current_pos, (y, x))
                    desired_angle = self.direction_map.get_angle(self.current_pos)
                    angle_diff = abs(angle - desired_angle)

                    if angle_diff > 3/2*np.pi:
                        angle_diff = abs(angle_diff - np.pi)
                    if distance <= self.max_step and angle_diff <= self.forward_move_angle / 2:
                        available_points.append((y, x))

        return available_points

    def move_price(self, pos: (int, int)) -> float:
        if self.direction_map.direction_map[pos[0]][pos[1]] == Env.EXIT:
            return 256
        price = (nav.get_distance_beteween_points(self.direction_map.get_next_position(self.current_pos), pos))
        price=price*nav.get_distance_beteween_points(pos,self.end[0])
        return np.floor(price)

    def get_best_move(self, moves):
        desired_move = self.direction_map.get_next_position(self.current_pos)

        if isinstance(desired_move, Env):
            return desired_move

        if self.collision_map[desired_move[0]][desired_move[1]] == 0:
            return desired_move

        if len(moves) == 0:
            print('stoje')
            return self.current_pos

        prices=list(map(lambda z: self.move_price(z),moves))
        mini = min(moves, key=lambda z: self.move_price(z))
        if mini==self.current_pos and len(moves)>1:
            print('Najlepiej to stac')
            print(self.current_pos)
            print(prices)
            print(moves)
            print(desired_move)
            print('KOniec')
        return mini

    def update_collisions(self, value):
        current_y, current_x = self.current_pos
        collision = self.front_collision_size
        for x in range(current_x - collision, current_x + collision + 1):
            for y in range(current_y - collision, current_y + collision + 1):
                mark_location((y, x), self.collision_map, value)

    def release_spce(self):
        self.update_collisions(-1)

    def block_space(self):
        self.update_collisions(1)

    def finished_reached(self, pos):
        pos = self.direction_map.direction_map[pos[0]][pos[1]]
        if isinstance(pos, Env) and pos == Env.EXIT:
            return True
        else:
            return False

    def move(self):
        self.release_spce()
        available_positions = self.get_possible_moves()

        random.shuffle(available_positions)

        best_pos = self.get_best_move(available_positions)

        if self.finished_reached(best_pos):
            raise ExitReached
        if best_pos == self.current_pos:
            self.anger += 1
        else:
            self.anger = 0
        self.update_facing_angle(best_pos)
        self.current_pos = best_pos
        self.block_space()

        return self.anger


class ExitReached(Exception):
    def __init__(self):
        super().__init__()
