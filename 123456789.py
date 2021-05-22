from pygame import *

back = (200, 255, 255)
win_width = 600
win_height = 500
window=display.set_mode((win_width,win_height))
window.fill(back)

clock = time.Clock()
FPS = 60
game = True
finish = False


class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x,player_y,player_speed,player_height,player_width):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(player_height,player_width))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y > - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y > - 80:
            self.rect.y += self.speed

racket1 = Player("rak.jpg", 30, 200, 4, 50, 150)
racket2 = Player("rak2.jpg", 520, 200, 4, 50, 150)
ball = GameSprite("fdhgdjg.jpg", 200, 200, 4, 50, 50)

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type==QUIT:
            game=False

            
    if finish != True:
        window.fill(back)   
        racket1.update_l()     
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        racket1.reset()    
        racket2.reset()
        ball.reset()
    if sprite.collide_rect(racket1, ball)  or sprite.collide_rect(racket2, ball):
            speed_x *= -1
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1     
    display.update()
    clock.tick(FPS)