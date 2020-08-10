from PIL import Image, ImageDraw, ImageEnhance, ImageChops, ImageFilter
from itertools import chain
import numpy as np
import random
import time

class Animation():

    def __init__(self, size, fire_nums):
        self.size = size
        self.fire_nums = fire_nums
        self.coords = np.random.randint(30, high=970, size=2*fire_nums).reshape(-1, 2)

    def create_decoration(self):
        for q in range(self.size):
            self.img = Image.new('RGB', (1000, 1000))
            self.draw = ImageDraw.Draw(self.img)
            for x in range(self.fire_nums):
                self.draw.rectangle([self.coords[x-1, 0], self.coords[x-1, 1], 
                    self.coords[x-1, 0]+q, self.coords[x-1, 1]+q], fill='white')

            self.blur = self.img.filter(ImageFilter.GaussianBlur(radius=10))
            self.output = ImageChops.lighter(self.img, self.blur)
            yield self.output
                

    def explode(self):
        self.coef = [0.2, 0.1, 0.1, 0.2, 0.4]
        self.ypoly = lambda x:(x*self.xpoly)**2
        self.colors = ['red', 'green', 'blue', 'yellow']
        self.x, self.y = self.coords[0]
        self.coef = np.random.uniform(0.1, 0.4, 5)
        for i in range(50):
            self.img = Image.new('RGB', (1000, 1000))
            self.draw = ImageDraw.Draw(self.img)
            self.xpoly = i*5
            for x in range(self.fire_nums):

                self.draw.rectangle([self.xpoly+self.x, 2*self.ypoly(self.coef[0])+self.y, 
                    self.xpoly+self.x+self.size, 2*self.ypoly(self.coef[0])+self.y+self.size], fill=random.choice(self.colors))       # center
                self.draw.rectangle([3*self.xpoly+self.x, 3*self.ypoly(self.coef[1])+self.y, 
                    3*self.xpoly+self.x+self.size, 3*self.ypoly(self.coef[1])+self.y+self.size], fill=random.choice(self.colors))     # right
                self.draw.rectangle([-3*self.xpoly+self.x, self.ypoly(self.coef[2])+self.y, 
                    -3*self.xpoly+self.x+self.size, self.ypoly(self.coef[2])+self.y+self.size], fill=random.choice(self.colors))      # bottom
                self.draw.rectangle([-3*self.xpoly+self.x, self.ypoly(self.coef[3])+self.y, 
                    -3*self.xpoly+self.x+self.size, self.ypoly(self.coef[3])+self.y+self.size], fill=random.choice(self.colors))      # left
                self.draw.rectangle([-2*self.xpoly+self.x, 0.5*self.ypoly(self.coef[4])+self.y, 
                    -2*self.xpoly+self.x+self.size, 0.5*self.ypoly(self.coef[4])+self.y+self.size], fill=random.choice(self.colors))  # top

            self.blur = self.img.filter(ImageFilter.GaussianBlur(radius=10))
            self.output = ImageChops.lighter(self.img, self.blur)
            yield self.output
            
animation = Animation(3, 1)
gif = list(chain(animation.create_decoration(), animation.explode()))

gif[0].save('Desktop/test.gif',
    save_all=True, append_images=gif, optimize=False, duration=50, loop=0)