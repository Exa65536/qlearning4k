__author__ = "Exa"

import numpy as np
from qlearning4k.games.game import Game
import copy


class TicTacToe(Game):
    def __init__(self, gridx, gridy):
        self.won = False
        self.over = False
        self.gridx = gridx
        self.gridy = gridy
        self.reset()

    def reset(self):
        self.state = np.zeros((self.gridx, self.gridy))
        self.won = False
        self.over = False

    @property
    def name(self):
        return "TicTacToe"

    @property
    def nb_actions(self):
        return self.gridx*self.gridy

    def haswon(self, player):
        state = self.state
        if max([all([state[i, j] == player for i in range(self.gridx)]) for j in range(self.gridy)]):
            return True
        if max([all([state[j, i] == player for i in range(self.gridy)]) for j in range(self.gridx)]):
            return True
        if self.gridx == self.gridy:
            if all([state[i,i] == player for i in range(self.gridx)]):
                return True
            if all([state[(self.gridx-1)-i, i] == player for i in range(self.gridx)]):
                return True
        return False

    def play(self, action):
        state = self.state
        if state[action // self.gridy, action % self.gridy] == 0:
            state[action // self.gridy, action % self.gridy] =1
        if np.count_nonzero(state) < self.gridx*self.gridy:
            moved = False
            while not moved:
                location = (np.random.randint(0, self.gridx), np.random.randint(0, self.gridy))
                if state[location] == 0:
                    moved = True
                    state[location] = .5
        if self.haswon(1):
            self.over = True
            self.won = True
        if self.haswon(.5):
            self.over = True
        if np.count_nonzero(state) == self.gridx*self.gridy:
            self.over = True
        self.state = state


    def get_state(self:
            return self.state


    def get_score(self):
        if self.haswon(1):
            self.won = True
            self.over=True
            return 1
        if self.haswon(.5):
            self.won = False
            self.over = True
            return -1
        else:
            return 0

    def is_over(self):
        return self.over

    def is_won(self):
        return self.wom
