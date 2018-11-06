import pygame, sys, random
from pygame.locals import *
from colors import *
import wall
import fruit
import worm

screenWidth, screenHeight = 800, 500

class Game():

    def getMotivationMessage(self):
            motivationMessages = ["Eat the fruit or die",
                        "Show them how to clean the room",
                        "Thrash the trash",
                        "Run!",
                        "Be happy",
                        "Be sad",
                        "Are you the snake or the worm?",
                        "Your mom isn't proud of you",
                        "You never got first place in anything",
                        "3.1415926535",
                        "Birds love you",
                        "This will never be like Earthworm Jim",
                        "You can be used as fertilizer, like garbage",
                        "More valuable than the argentine peso",
                        "Faster than the devaluation of the argentine peso",
                        "Strill trying?",
                        "At least that was a good death",
                        "C'mon, give up!",
                        "You'll never know what awaits you at the end"]
            randMessage = random.randint(0, len(motivationMessages) - 1)
            return  motivationMessages[randMessage]
    def getDeathSound(self):
        deathSounds = ["death1.ogg", "death2.ogg"]
        randDeathSound = random.randint(0, len(deathSounds) - 1)
        return deathSounds[randDeathSound]

    def getEatFruitSound(self):
        eatFruitSounds = ["win1.ogg", "win2.ogg"]
        randEatFruitSounds = random.randint(0, len(eatFruitSounds) - 1)
        return eatFruitSounds[randEatFruitSounds]

    def __init__(self):
        self.score = 0
        self.font = "joystixMonospace.ttf"
        self.motivationMessage = self.getMotivationMessage()
        self.deathSound = pygame.mixer.Sound(self.getDeathSound())
        self.eatFruitSound = pygame.mixer.Sound(self.getEatFruitSound())
        self.gameOver = False
        self.frameDim = (400, 400)
        self.margin = 10
        self.player = worm.Worm(self.frameDim[0] // 2,
                                self.frameDim[1] // 2,
                                1)
        self.fruit = fruit.Fruit(random.randint(self.margin,
                                 self.frameDim[0]),
                                 random.randint(1, self.frameDim[1]))

        ############################### REVISAR ##############################
        self.frame = [wall.Wall(self.margin, self.margin, self.frameDim[0], 1),
                      wall.Wall(self.margin, self.margin, 1, self.frameDim[1]),
                      wall.Wall(self.margin, self.frameDim[0] +
                                self.margin, self.frameDim[0],1),
                      wall.Wall(self.frameDim[0] + self.margin, self.margin,
                                1, self.frameDim[1])]
        ######################################################################

        self.allSpriteList = pygame.sprite.Group()
        self.wallList = pygame.sprite.Group()
        self.fruitList = pygame.sprite.Group()
        self.allSpriteList.add(self.player.segments, self.fruit, self.frame)
        self.wallList.add(self.frame)
        self.fruitList.add(self.fruit)

    def processEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True
                elif event.key == K_UP or event.key == K_w:
                    self.player.changeDxDy(0, -self.player.dimension)
                elif event.key == K_DOWN or event.key == K_s:
                    self.player.changeDxDy(0, self.player.dimension)
                elif event.key == K_LEFT or event.key == K_a:
                    self.player.changeDxDy(-self.player.dimension, 0)
                elif event.key == K_RIGHT or event.key == K_d:
                    self.player.changeDxDy(self.player.dimension, 0)
                elif event.key == K_SPACE:
                    if self.gameOver:
                        self.__init__()
        return False

    def checkPlayerFruitCollision(self):
        for segment in self.player.segments:
            hitList = pygame.sprite.spritecollide(segment, self.fruitList,
                                                  False)
            if len(hitList) != 0:
                self.score += 1
                self.fruit.changePosition(random.randint(self.margin,
                                          self.frameDim[0]),
                                          random.randint(self.margin,
                                          self.frameDim[1]))
                self.allSpriteList.add(self.player.addSegment())
                self.eatFruitSound.play()

    def checkPlayerFrameCollision(self):
        for segment in self.player.segments:
            hitList = pygame.sprite.spritecollide(segment, self.frame, False)
            if len(hitList) != 0:
                self.score = 0
                self.deathSound.play()
                return True
            return False

    def drawText(self, font, fontSize, text, screen,
                 pos=(screenWidth // 2, screenHeight // 2)):
        font = pygame.font.Font(font, fontSize)
        text = font.render(text, True, WHITE)
        centerX = pos[0] - (text.get_width() // 2)
        centerY = pos[1] - (text.get_height() // 2)
        screen.blit(text, [centerX, centerY])

    def showGameOverScreen(self, screen):
        self.drawText(self.font, 40, "GAME OVER!", screen)
        self.drawText(self.font, 20,
                      "Press SPACE to play again or ESC to quit",
                       screen, (screenWidth // 2,
                       (screenHeight + 60) // 2))

    def showMotivation(self, screen):
        self.drawText(self.font, 15, self.motivationMessage,
                      screen, (screenWidth // 2, screenHeight - 70))

    def showScore(self, screen):
        self.drawText(self.font, 30, "SCORE " + str(self.score),
                      screen, (screenWidth - 200, screenHeight - 485))

    def showInstructions(self, screen):
        self.drawText(self.font, 15, "Move with the arrow keys or WASD",
                      screen, (screenWidth // 2, screenHeight - 50))
        self.drawText(self.font, 15, "Press ESC to quit", screen,
                      (screenWidth // 2, screenHeight - 20))

    def runLogic(self):
        if not self.gameOver:
            self.allSpriteList.update()
            self.checkPlayerFruitCollision()
            self.gameOver = self.checkPlayerFrameCollision()

    def displayFrame(self, screen, color=BLACK):
        screen.fill(color)
        if not self.gameOver:
            self.allSpriteList.draw(screen)
            self.showMotivation(screen)
            self.showScore(screen)
            self.showInstructions(screen)
        if self.gameOver:
            self.showGameOverScreen(screen)
        pygame.display.flip()

def terminate():
    pygame.quit()
    sys.exit()

def main():
    fps = 4
    pygame.init()
    screenSurf = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("WORMUNGER")
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    game = Game()
    done = False
    while not done:
        done = game.processEvents()
        game.runLogic()
        game.displayFrame(screenSurf)
        clock.tick(fps)
    terminate()

if __name__ == "__main__":
    main()
