import pygame
from paddle import Paddle
from ball import Ball
from queue import Queue


class Pong:


    def __init__(self, color1=(0, 0, 0), color2=(255, 255, 255), size=(700, 500), ai_player_count=1):
        self.color1 = color1
        self.color2 = color2
        self.size = (700, 500)
        self.screen = pygame.display.set_mode(size)
        self.ai_player_count = ai_player_count # TODO: Make this variable useful.
        self.ai_key_press = []


    def get_ai_key_press(self):
        event = self.ai_key_press
        self.ai_key_press = None
        return event

    def set_ai_key_press(self, key):
        self.ai_key_press

    def play(self):
        pygame.display.set_caption("Pong")
        pygame.init()
        paddleA = Paddle(self.color2, 10, 100)
        paddleA.rect.x = 20
        paddleA.rect.y = 200

        paddleB = Paddle(self.color2, 10, 100)
        paddleB.rect.x = 670
        paddleB.rect.y = 200

        ball = Ball(self.color2, 10, 10)
        ball.rect.x = 345
        ball.rect.y = 195

        # This will be a list that will contain all the sprites we intend to use in our game.
        all_sprites_list = pygame.sprite.Group()

        # Add the 2 paddles and the ball to the list of objects
        all_sprites_list.add(paddleA)
        all_sprites_list.add(paddleB)
        all_sprites_list.add(ball)

        # The loop will carry on until the user exits the game (e.g. clicks the close button).
        carryOn = True

        # The clock will be used to control how fast the screen updates
        clock = pygame.time.Clock()

        # Initialise player scores
        scoreA = 0
        scoreB = 0

        # -------- Main Program Loop -----------
        while carryOn:
            # --- Main event loop
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    carryOn = False  # Flag that we are done so we exit this loop
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                        carryOn = False

            # Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                paddleA.moveUp(5)
            if keys[pygame.K_s]:
                paddleA.moveDown(5)
            if keys[pygame.K_UP]:
                paddleB.moveUp(5)
            if keys[pygame.K_DOWN]:
                paddleB.moveDown(5)



                # --- Game logic should go here
            all_sprites_list.update()

            # Check if the ball is bouncing against any of the 4 walls:
            if ball.rect.x >= 690:
                scoreA += 1
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.x <= 0:
                scoreB += 1
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.y > 490:
                ball.velocity[1] = -ball.velocity[1]
            if ball.rect.y < 0:
                ball.velocity[1] = -ball.velocity[1]

                # Detect collisions between the ball and the paddles
            if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
                ball.bounce()

            # --- Drawing code should go here
            # First, clear the screen to black.
            self.screen.fill(self.color1)
            # Draw the net
            pygame.draw.line(self.screen, self.color2, [349, 0], [349, 500], 5)

            # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
            all_sprites_list.draw(self.screen)

            # Display scores:
            font = pygame.font.Font(None, 74)
            text = font.render(str(scoreA), 1, self.color2)
            self.screen.blit(text, (250, 10))
            text = font.render(str(scoreB), 1, self.color2)
            self.screen.blit(text, (420, 10))

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
        pygame.quit()