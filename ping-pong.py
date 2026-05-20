from pygame import *
init()

sos = display.set_mode((677,677))


class Player():
   def __init__(self, x,y,w,h,speed):
       self.hitbox = Rect(x,y,w,h)
       self.speed = speed
   def move(self):
        
        key_list = key.get_pressed()
        if key_list[K_DOWN] == True:
            self.hitbox.y += self.speed
        elif key_list[K_UP] == True:
            self.hitbox.y -= self.speed

   def hit(self):




player1 = Player(250,250,20,100,5)
red = (150, 10, 10)
ball = Ball(744,320,4,5,2,3)




class Ball():
    def _init_(self, x,y,w,h, x_speed, y_speed):
        self.hitbox = Rect(x,y,w,h)
        self.x_speed = x_speed
        self. y_speed = y_speed
    def move(self):
        self.hitbox.x += self.x_speed
        self.hitbox. y += self.y_speed
        if self.hitbox.x > 677- self.hitbox.width:
            self.y_speed = -self.y_speed
            self.x_speed = -self.x_speed































while True:
    
    eventlist = event.get()
    draw.rect(sos,red,player1.hitbox)
    player1.move()
    sos.fill((10,10,100))
    for e in eventlist:
        if e.type == QUIT:
            exit()
    draw.rect(sos,white,ball.hitbox)
    Ball.move()
    display.update()
    time.Clock().tick(180)