import threading

from pong import Pong
import time
import torch
import pygame
import tensorflow as tf
import random
from collections import deque
from model import Linear_QNet, QTrainer
import numpy as np
from torchvision import transforms

# from PIL import Image
from numpy import asarray


MAX_MEMORY = 100_000
BATCH_SIZE = 1000
NUM_ITERATIONS = 1000000
LR = 0.001

class Agent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 0  # randomness
        self.gamma = 0  # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)  # popleft() on max memory
        self.model = Linear_QNet(3, 256, 2)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)
    def get_action(self, state):
        move_options = ["UP", "DOWN"]
        # random moves: tradeoff exploration / exploitation
        self.epsilon = 80 - self.n_games

        final_move = [0, 0]
        # random moves: tradeoff exploration / exploitation

        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 1)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state.copy(), dtype=torch.float)
            prediction = self.model(state0)
            # print(f"prediction is {prediction}")

            move = torch.argmax(prediction).item()

            print(f"Move value is {move}")

            final_move[move] = 1

            print(f"final_move value is {final_move} : {final_move[move]}")

        return final_move

    def get_state(self, game):

        current_screen = pygame.surfarray.pixels3d(game.screen)

        return current_screen

def train():

    game = Pong(ai_player_count=1)
    agent = Agent()

    carryOn = True
    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                carryOn = False  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                    carryOn = False

        game.play_turn(agent.get_action(agent.get_state(game)))

    agent.get_state(game)

    game.end_game()

if __name__ == '__main__':
    train()