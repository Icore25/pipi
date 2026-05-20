from pygame import *
init()

window = display.set_mode((677,677))


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


player1 = Player(250,250,20,100,5)
red = (150, 10, 10)


























while True:
    eventlist = event.get()
    draw.rect(window, red, player1.hitbox)
    player1.move()
    
    for e in eventlist:
        if e.type == QUIT:
            exit()
    

    display.update()
    time.Clock().tick(180)