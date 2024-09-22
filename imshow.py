import pygame
from preprocessing.filter import outline_filter
from PIL import Image
import numpy as np
import cv2
class imshow:
    def __init__(self,resolution):
        self.resolution=resolution
        print(self.resolution)
        pygame.init()
        self.screen = pygame.display.set_mode((500,500),pygame.RESIZABLE)
        pygame.display.set_caption('dan')
        self.resize = self.get_resize(self.resolution,self.screen.get_size())
    
    def __call__(self,img):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                status = False
            if i.type==pygame.VIDEORESIZE:
                self.resize = self.get_resize(self.resolution,i.size)
        screen_update = pygame.surfarray.make_surface(np.flipud(np.rot90(cv2.cvtColor(img,cv2.COLOR_BGRA2RGB),1)))
        screen_update = pygame.transform.scale(screen_update,self.resize)
        
        self.screen.blit(screen_update, (0,0))
        pygame.display.flip()


    def get_resize(self,curr,goal):
        new_curr = curr[0]/curr[1]
        new_goal = goal[0]/goal[1]
        if new_curr>new_goal:
            return (goal[0], curr[1]*goal[0]/curr[0])
        elif new_curr<new_goal:
            return (curr[0]*goal[1]/curr[1], goal[1])
        else:
            return goal
"""imshower = imshow((1024,576))
data,picture=outline_filter(Image.open("C:/Users/Admin/Downloads/Purple-1024x576.jpg"),0,300)
imshower.update(picture)

while True:
    next
"""