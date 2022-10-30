import pygame
from paddle import Paddle
from ball import Ball
import copy
import queue
from queue import Queue
import random


class Pong:


    def __init__(self, color1=(0, 0, 0), color2=(255, 255, 255), size=(700, 500), ai_player_count=1, ai_1_queue=None):
        self.color1 = color1
        self.color2 = color2
        self.size = (700, 500)
        self.screen = pygame.display.set_mode(size)
        self.ai_player_count = ai_player_count # TODO: Make this variable useful.
        self.ai_move = [0, 0]
        self.ai_1_queue = ai_1_queue
        pygame.display.set_caption("Pong")
        pygame.init()
        self.paddleA = Paddle(self.color2, 10, 100)
        self.paddleA.rect.x = 20
        self.paddleA.rect.y = 200

        self.paddleB = Paddle(self.color2, 10, 100)
        self.paddleB.rect.x = 670
        self.paddleB.rect.y = 200

        self.ball = Ball(self.color2, 10, 10)
        self.ball.rect.x = 345
        self.ball.rect.y = 195

        # This will be a list that will contain all the sprites we intend to use in our game.
        self.all_sprites_list = pygame.sprite.Group()

        # Add the 2 paddles and the ball to the list of objects
        self.all_sprites_list.add(self.paddleA)
        self.all_sprites_list.add(self.paddleB)
        self.all_sprites_list.add(self.ball)

        # The loop will carry on until the user exits the game (e.g. clicks the close button).


        # The clock will be used to control how fast the screen updates
        self.clock = pygame.time.Clock()

        self.scoreA = 0
        self.scoreB = 0

    def end_game(self):
        pygame.quit()



    def play_turn(self, action):
        # Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B)
        keys = pygame.key.get_pressed()
        if self.ai_player_count == 0:
            if keys[pygame.K_w]:
                self.paddleA.moveUp(5)
            if keys[pygame.K_s]:
                self.paddleA.moveDown(5)
            if keys[pygame.K_UP]:
                self.paddleB.moveUp(5)
            if keys[pygame.K_DOWN]:
                self.paddleB.moveDown(5)
        if self.ai_player_count == 1:
            if action == "UP":
                self.paddleA.moveUp(5)
            if action == "DOWN":
                self.paddleA.moveDown(5)
            if keys[pygame.K_UP]:
                self.paddleB.moveUp(5)
            if keys[pygame.K_DOWN]:
                self.paddleB.moveDown(5)

            # --- Game logic should go here
        self.all_sprites_list.update()

        # Check if the ball is bouncing against any of the 4 walls:
        if self.ball.rect.x >= 690:
            self.scoreA += 1
            self.ball.velocity[0] = -self.ball.velocity[0]
        if self.ball.rect.x <= 0:
            self.scoreB += 1
            self.ball.velocity[0] = -self.ball.velocity[0]
        if self.ball.rect.y > 490:
            self.ball.velocity[1] = -self.ball.velocity[1]
        if self.ball.rect.y < 0:
            self.ball.velocity[1] = -self.ball.velocity[1]

            # Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(self.ball, self.paddleA) or pygame.sprite.collide_mask(self.ball, self.paddleB):
            self.ball.bounce()

        # --- Drawing code should go here
        # First, clear the screen to black.
        self.screen.fill(self.color1)
        # Draw the net
        pygame.draw.line(self.screen, self.color2, [349, 0], [349, 500], 5)

        # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        self.all_sprites_list.draw(self.screen)

        # Display scores:
        font = pygame.font.Font(None, 74)
        text = font.render(str(self.scoreA), 1, self.color2)
        self.screen.blit(text, (250, 10))
        text = font.render(str(self.scoreB), 1, self.color2)
        self.screen.blit(text, (420, 10))

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        self.clock.tick(60)

        return self.scoreA

# Once we have exited the main program loop we can stop the game engine:
