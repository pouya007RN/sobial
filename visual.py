import pygame , random 
import time




class bar :
        def __init__(self, value , x=0):
                self.v = value
                self.x = x


        def forward(self):
                #for i in range (80):
                self.x +=1


        def backward(self):
                self.x -=1
                

        



def draw (bar ,surface ):
    pygame.draw.rect( surface , (bar.v ,0,0) , ( bar.x , 490 , 20 ,-1*bar.v))




def switch (bar1 , bar2 ,flat):

        for i in range (80):
                flat.fill((0,0,0))
                draw (bar0 , flat)
                draw (bar1 , flat )
                draw (bar2 , flat )
                draw (bar3 , flat )
                draw (bar4 , flat )
                draw (bar5 , flat )
                draw (bar6 , flat )
                draw (bar7 , flat )
                draw (bar8 , flat )
                draw (bar9 , flat )
                time.sleep(0.01)
        
                bar1.forward()
                bar2.backward()
                pygame.display.update()
        




pygame.init()
fw = 800
fh = 500
flat = pygame.display.set_mode((fw , fh))

randnum = []
bars = []


x0=0
x1 = 80
x2 = 160
x3 = 240
x4 = 320
x5 = 400
x6 = 480
x7 = 560
x8 = 640
x9 = 720



for i in range (10):
        
	bars.append(bar( random.randint(0,244) , x0))





for i in range (10):
        randnum.append(random.randint(0,255))

   


bar0 = bar( randnum[0] , x0)
bar1 = bar( randnum[1] , x1)
bar2 = bar( randnum[2] , x2)
bar3 = bar( randnum[3] , x3)
bar4 = bar( randnum[4] , x4)
bar5 = bar( randnum[5] , x5)
bar6 = bar( randnum[6] , x6)
bar7 = bar( randnum[7] , x7)
bar8 = bar( randnum[8] , x8)
bar9 = bar( randnum[9] , x9)



t= 0
switch (bar5 , bar6 , flat)
bar5 =bar6 and bar6 = bar5

switch (bar5 , bar7 , flat)


	
