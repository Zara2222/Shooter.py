from pygame import*
from random import randint
import time as my_time
WINDOW_SIZE = (700, 500)
FPS = 60
SPSize = (65, 65)
White = (255, 255, 255)

bullets = sprite.Group()

window = display.set_mode(WINDOW_SIZE)

font.init()
font_counter = font.Font(None, 24)
font_message = font.Font(None, 70)

interval = 0.3 
fire_time = 0


class Counter:
    def __init__(self, fontObj, color):
        self.lost = 0
        self.killed = 0
        self.fontObj = fontObj
        self.color = color
    def show(self):
        self.lostObj = self.fontObj.render("Пропущено: " +  str (self.lost), 1, self.color)
        window.blit(self.lostObj, (0,0))
        self.killedObj = self.fontObj.render("Да ты крут!: " + str (self.killed), 1, self.color )
        window.blit(self.killedObj, (0,30))

counter = Counter(font_counter, White)

class GameSprite(sprite.Sprite):
    def __init__(self, playerImage, playerX, playerY, playerSpeed):
        super().__init__()
        self.image= transform.scale(image.load(playerImage), SPSize)
        self.playerSpeed = playerSpeed
        self.rect = self.image.get_rect()
        self.rect.x = playerX
        self.rect.y = playerY

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_position(self):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.playerSpeed
        if keys[K_RIGHT] and self.rect.x < WINDOW_SIZE[0] - SPSize[0] :
            self.rect.x += self.playerSpeed    

    def fire(self):
        global fire_time
        keys = key.get_pressed()
        if keys [K_SPACE] and my_time.time() > fire_time + interval:
            fire_time = my_time.time()
            bullet = Bullet('bullet.png', self.rect.x ,  self.rect.y , 5)
            bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        global lost_enemy
        if self.rect.y < WINDOW_SIZE[1]:
            self.rect.y += self.playerSpeed
        else:
            self.rect.y = 0
            self.rect.x = randint(0, WINDOW_SIZE[0] - SPSize[0])
            counter.lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.playerSpeed
        if self.rect.y <= 0:
            self.kill()
