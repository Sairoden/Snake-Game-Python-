import pygame
import random


FPS = 10
windowWidth = 600
windowHeight = 400
boxSize = 25

boxWidth = windowWidth / boxSize
boxHeight = windowHeight / boxSize

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game by Sairoden Gandarosa")
        self.window = pygame.display.set_mode((windowWidth, windowHeight))
        self.clock = pygame.time.Clock()
        self.running = True
        self.directionX = 1
        self.directionY = 0
        self.startX = random.randint(6, boxWidth - 6)
        self.startY = random.randint(6, boxHeight - 6)
        self.snakeBody = [{'x': self.startX, 'y': self.startY},
                          {'x': self.startX - 1, 'y': self.startY}]

        self.foodPosition = self.randomlocation()

    def runGame(self):
        self.window.fill(BLACK)
        self.drawGrid()
        self.move()
        self.events()
        self.drawSnake(self.snakeBody)
        self.drawFood(self.foodPosition)
        pygame.display.update()
        self.clock.tick(FPS)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            keys = pygame.key.get_pressed()
            for key in keys:
                if key[pygame.K_RIGHT]:
                    self.directionX = 1
                    self.directionY = 0

                elif keys[pygame.K_LEFT]:
                    self.directionX = -1
                    self.directionY = 0

                elif keys[pygame.K_UP]:
                    self.directionX = 0
                    self.directionY = -1

                elif keys[pygame.K_DOWN]:
                    self.directionX = 0
                    self.directionY = 1

            if not(self.snakeBody[0]['x'] == self.foodPosition['x'] and self.snakeBody[0]['y'] == self.foodPosition['y']):
                self.snakeBody.pop(-1)

            else:
                self.foodPosition == self.randomlocation()

            if self.snakeBody[0]['x'] == -1 or self.snakeBody[0]['y'] == -1 or self.snakeBody[0]['x'] == boxWidth or self.snakeBody[0]['y'] == boxHeight:
                self.gameOver()
                self.reset()

            for collide in self.snakeBody[1:]:
                if (self.snakeBody[0]['x'] == collide['x'] and self.snakeBody[0]['y'] == collide ['y']):
                    self.gameOver()
                    self.reset()

    def move(self):
        self.snakeBody.insert(0, {'x': self.snakeBody[0]['x'] + self.directionX, 'y': self.snakeBody[0]['y'] + self.directionY})

    def drawGrid(self):
        for x in range (0, windowWidth, boxSize):
            for y in range (0, windowHeight, boxSize):
                pygame.draw.line(self.window, (50, 50, 50), (x, 0), (x, windowHeight))
                pygame.draw.line(self.window, (50, 50, 50), (0, y), (windowWidth, y))

    def drawSnake(self, position):
        for pos in position:
            x = pos['x'] * boxSize
            y = pos['y'] * boxSize
            snakeRect = pygame.Rect(x, y, boxSize, boxSize)
            pygame.draw.rect(self.window, GREEN, snakeRect)

    def drawFood(self, position):
        x = position['x'] * boxSize
        y = position['y'] * boxSize
        foodRect = pygame.Rect(x, y, boxSize, boxSize)
        pygame.draw.rect(self.window, RED, foodRect)


    def randomlocation(self):
        return {'x': random.randint(0, boxWidth - 1), 'y': random.randint(0, boxHeight - 1)}

    def drawText(self, text, size, color, x, y):
        font = pygame.font.Font("freesansbold.ttf", size)
        fontSurface = font.render(text, True, color)
        fontRect = fontSurface.get_rect()
        fontRect.midtop = (x, y)
        self.window.blit(fontSurface, fontRect)

    def waitKey(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False

                if event.type == pygame.KEYUP:
                    waiting = False

        return waiting

    def startScreen(self):
        self.window.fill(BLACK)
        self.drawText("Snake Game by Sairoden Gandarosa", 25, (255, 255, 255), windowWidth / 2, windowHeight / 2)
        pygame.display.update()
        self.waitKey()


    def gameOver(self):
        self.window.fill(BLACK)
        self.drawText("Game Over\nThanks for playing!", 25, (255, 255, 255), windowWidth / 2, windowHeight / 2)
        pygame.display.update()
        self.waitKey()

    def reset(self):
        self.snakeBody = [{'x': self.startX, 'y': self.startY},
                          {'x': self.startX - 1, 'y': self.startY}]
        self.foodPosition = self.randomlocation()


game = Game()
game.startScreen()
while game.running:
    game.runGame()

pygame.quit()
