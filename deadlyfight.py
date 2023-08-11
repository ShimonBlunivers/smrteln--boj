import pygame
import random
import sys

from pygame.locals import *

pygame.init()

pygame.mixer.init()

pygame.display.set_caption('Deadly Fight')

clock = pygame.time.Clock()

resolution = (540, 720)

screen = pygame.display.set_mode(resolution)

class World:
    def __init__(self):
        self.color = [20, 40, 60]
        self.game = True
        self.death = False

    def screenFill(self):
        screen.fill((self.color))
        
    def update(self):
        self.screenFill()
        player1.update()
        pygame.display.update()

class player:
    def __init__(self):
        self.idleFrames = [pygame.image.load('files\idle\idle1.png'), pygame.image.load('files\idle\idle2.png'), pygame.image.load('files\idle\idle3.png'), pygame.image.load('files\idle\idle4.png')]
        self.punchFrames = [pygame.image.load('files\punch\punch1.png'), pygame.image.load('files\punch\punch2.png'), pygame.image.load('files\punch\punch3.png'), pygame.image.load('files\punch\punch4.png'), pygame.image.load('files\punch\punch5.png')]
        self.currentFrame = pygame.image.load('files\idle\idle1.png')
        self.currentFrameID = 0
        self.lastUpdated = 0
        self.state = 'idle'
        self.actionInProgress = False

    def render(self):   
        screen.blit(self.currentFrame, (0 ,100 ))

    def animate(self):
        now = pygame.time.get_ticks()
        if self.state == 'idle':
            if now - self.lastUpdated > 400:
                self.lastUpdated = now
                self.currentFrame = self.idleFrames[random.randint(0,3)]

                # try:
                #     self.currentFrame = self.idleFrames[self.currentFrameID]
                #     self.currentFrameID += 1
                # except:
                #     self.currentFrameID = 0
                #     self.currentFrame = self.idleFrames[self.currentFrameID]
                #     self.currentFrameID += 1
        if self.state == 'punch':
            if now - self.lastUpdated > 400:
                self.lastUpdated = now
                try:
                    self.currentFrame = self.punchFrames[self.currentFrameID]
                    self.currentFrameID += 1
                    if self.currentFrameID == 3:
                        sound = pygame.mixer.Sound('files\punch\hit.mp3')
                        sound.play()
                except:
                    self.currentFrameID = 1
                    self.currentFrame = self.idleFrames[0]
                    self.state = 'idle'
                    self.actionInProgress = False

    def update(self):
        self.render()
        self.control()

    def control(self):
        self.animate()
        keys = pygame.key.get_pressed()

        if keys[K_f] and not self.actionInProgress:
            self.state = 'punch'
            self.currentFrameID = 0
            self.actionInProgress = True


world = World()

player1 = player()

while world.game:
    clock.tick(60)

    world.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            world.game = False
            pygame.quit()
            sys.exit()
