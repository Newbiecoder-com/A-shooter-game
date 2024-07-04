#Create your own shooter

from pygame import *
from random import *

window = display.set_mode((700, 500))
display.set_caption('Shooter game')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))



bullets = sprite.Group()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


bullets = sprite.Group()
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.x < 625:
            self.rect.x += self.speed
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
   
    def fire(self):

        bullet = Bullet('bullet.png', self.rect.x+ 35, 450, 10, 30, 30)
        bullets.add(bullet)





speed = 5

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global missed
        if self.rect.y > 500:
           self.rect.y = 0
           missed += 1
           self.rect.y         
            


ufos = sprite.Group()
for i in range(4):
    ufo = Enemy('ufo.png', randint(0, 600), 0, randint(1,5), 100, 80)
    ufos.add(ufo)


'''
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
'''

ship = Player('rocket.png', 10, 390, 10, 50, 80)

clock = time.Clock()
FPS = 60 

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed





font.init()
font1 = font.Font(None, 50)


finish = False

missed = 0
score_point = 0

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False       
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship .fire()
    
    
    if not finish:

        window.blit(background,(0, 0))


        ship.reset()
        ship.update()

        ufos.draw(window)
        ufos.update()

        bullets.draw(window)
        bullets.update()
    
    missed_aliens = font1.render('MISSED'+ str(missed), True, (255, 255, 255))
    window.blit(missed_aliens, (20, 30))
    
    font2 = font.Font(None, 30)
    score = font2.render('SCORE:'+ str(score_point), True, (255, 255, 255))
    
    window.blit(score,(50, 60))

    collides = sprite.groupcollide(ufos, bullets, True, True)
    for col in collides:
        ufo = Enemy('ufo.png', randint(0, 600), 0, randint(0, 5), 80, 80)
        ufos.add(ufo)
        score_point += 1


    if sprite.spritecollide(ship, ufos, False)or missed >= 5:
        window.blit(lose, (300, 200))
        finish = True













    clock.tick(FPS)
    display.update()