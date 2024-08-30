import pygame
from preprocessing.filter import outline_filter
from PIL import Image
import numpy as np
import cv2
class imshow:
    def __init__(self,resolution):
        pygame.init()
        self.screen = pygame.display.set_mode((500,500),pygame.RESIZABLE)
        pygame.display.set_caption('dan')
    def __call__(self,img):
        self.screen.blit(pygame.surfarray.make_surface(np.flipud(np.rot90(cv2.cvtColor(img,cv2.COLOR_BGRA2RGB),1))), (0,0))
        pygame.display.update()


"""imshower = imshow((1024,576))
data,picture=outline_filter(Image.open("C:/Users/Admin/Downloads/Purple-1024x576.jpg"),0,300)
imshower.update(picture)

while True:
    next
"""