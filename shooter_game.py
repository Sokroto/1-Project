#Создай собственный Шутер!
# ! Deprecated method, do not use
from pygame import *
from random import *
import time as tm
font.init()
font1 = font.SysFont('Arial', 36)
window = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
clock = time.Clock()
FPS = 60
lost = 0
find = 0
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
class GameSprite(sprite.Sprite):
    def __init__(self, image_pic, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_pic), (65, 65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_RIGHT]:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[K_d]:
            self.rect.x += self.speed
        if keys_pressed[K_a]:
            self.rect.x -= self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx-25, self.rect.top, 50)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(80, 700-80)
            self.speed = randint(1, 4)
            self.rect.y = 0
            lost = lost+1
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(80, 700-80)
            self.speed = randint(1, 4)
            self.rect.y = 0
spr = Player('rocket.png', 0, 400, 5)
bullets = sprite.Group()
monster = Enemy('ufo.png', 5, 0, 2)
monster2 = Enemy('ufo.png', 70, 0, 1)
monster3 = Enemy('ufo.png', 140, 0, 1)
monster4 = Enemy('ufo.png', 210, 0, 3)
monster5 = Enemy('ufo.png', 280, 0, 2)
asteroid = Asteroid('asteroid.png', 200, 0, 1.5)
asteroid3 = Asteroid('asteroid.png', 400, 0, 1.5)
asteroid2 = Asteroid('asteroid.png', 37, 0, 1.5)
asteroids = sprite.Group()
asteroids.add(asteroid)
asteroids.add(asteroid2)
asteroids.add(asteroid3)
monsters = sprite.Group()
monsters.add(monster)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)
game = True
while game:
    clock.tick(FPS)
    window.blit(background, (0, 0))
    spr.reset()
    spr.update()
    asteroids.draw(window)
    asteroids.update()
    bullets.draw(window)
    bullets.update()
    monsters.draw(window)
    monsters.update()
    text_lose = font1.render('Пропущено:'+ str(lost), 1, (255, 255, 255))
    text_find = font1.render('Попал:'+ str(find), 1, (255, 255, 255))
    window.blit(text_lose, (500, 50))
    window.blit(text_find, (500, 100))
    spr_list = sprite.spritecollide(spr, monsters, False)
    dlina = len(spr_list)
    spr2_list = sprite.groupcollide(monsters, bullets, True, True)
    spr3_list = sprite.spritecollide(spr, asteroids, False)
    dlina2 = len(spr3_list)
    if lost >= 5 or dlina != 0 or dlina2 != 0:
        text_gameover = font1.render('Game Over!:'+ str(lost), 1, (255, 255, 255))
        window.blit(text_gameover, (200, 200))
        display.update()
        tm.sleep(5)
        break
    if find >= 15:
        text_gameover = font1.render('You Win !:'+ str(lost), 1, (255, 255, 255))
        window.blit(text_gameover, (200, 200))
        display.update()
        tm.sleep(5)
        break
    for i in spr2_list:
        find +=1
        monster6 = Enemy('ufo.png', randint(80, 700-80), 0, randint(1, 4))
        monsters.add(monster6)
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                spr.fire()
    display.update()
