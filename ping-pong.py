from pygame import *
init()

sos = display.set_mode((677,677))


class Player():
    def __init__(self, x,y,w,h,speed):
       self.hitbox = Rect(x,y,w,h)
       self.speed = 2
    def move(self):
        key_list = key.get_pressed()
        if key_list[K_DOWN] == True:
            self.hitbox.y += self.speed
        elif key_list[K_UP] == True:
            self.hitbox.y -= self.speed

    def hit(self):
       if self.hitbox.colliderect(ball.hitbox): 
            ball.x_speed = -ball.x_speed
    def pilot(self):
        if ball.hitbox.y > self.hitbox.y:
            self.speed = 2
        else:
            self.speed = -2
        self.hitbox.y += self.speed
        
    



player2 = Player(660,350,20,100,5)
player1 = Player(0,350,20,100,5)
red = (150, 10, 10)
white = (255,255,255)





class Ball():
    def __init__(self, x,y,w,h, x_speed, y_speed):
        self.hitbox = Rect(x,y,w,h)
        self.x_speed = x_speed
        self. y_speed = y_speed
    def move(self):
        self.hitbox.x += self.x_speed
        self.hitbox. y += self.y_speed
        if self.hitbox.x > 677- self.hitbox.width:
            self.x_speed = -self.x_speed
            self.hitbox.x = 300
            self.hitbox.y = 300

        if self.hitbox.y > 677- self.hitbox.height:
            self.y_speed = -self.y_speed
            
            
        if self.hitbox.x < 0 :
            self.x_speed = -self.x_speed
            self.hitbox.x = 300
            self.hitbox.y = 300
            
        if self.hitbox.y < 0 :
            self.y_speed = -self.y_speed
            
ball = Ball(300,300,15,15,3,3)
































while True:

    sos.fill((10,10,100))
    eventlist = event.get()
    draw.rect(sos,red,player1.hitbox)
    draw.rect(sos,red,player2.hitbox)
    player1.move()
    player1.hit()
    player2.pilot()
    player2.hit()
    
    
    for e in eventlist:
        if e.type == QUIT:
            exit()
    draw.rect(sos,white,ball.hitbox)
    ball.move()
    
    display.update()
    time.Clock().tick(180)
    