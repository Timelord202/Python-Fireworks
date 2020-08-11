from PIL import Image, ImageDraw, ImageChops, ImageFilter
from itertools import chain
import numpy as np
import random

class Animation:
    def __init__(self, size):
        self.size = size 
        self.x, self.y = np.random.randint(200 , 800, size=2)

    def create_decoration(self):
        for q in range(3):
            self.img = Image.new('RGB', (1000, 1000))
            self.draw = ImageDraw.Draw(self.img)

            self.draw.rectangle([self.x, self.y, 
                self.x+q, self.y+q], fill='white')

            self.blur = self.img.filter(ImageFilter.GaussianBlur(radius=10))
            self.output = ImageChops.lighter(self.img, self.blur)
            yield self.output

    def main(self):
        self.colors = ['red', 'green', 'blue', 'yellow']
        self.ypoly = lambda x:(x*self.xpoly)**2
        self.coefs = np.random.uniform(0.2, 0.5, 5)

        for i in range(15):
            self.img = Image.new('RGB', (1000, 1000))
            self.draw = ImageDraw.Draw(self.img)
            self.xpoly = i*5

            # Draw the explosions
            self.draw.rectangle([self.xpoly+self.x, self.ypoly(self.coefs[0])+self.y, 
                self.xpoly+self.x+self.size, self.ypoly(self.coefs[0])+self.y+self.size], fill=random.choice(self.colors))      
            self.draw.rectangle([self.xpoly+self.x, self.ypoly(self.coefs[1])+self.y, 
                self.xpoly+self.x+self.size, self.ypoly(self.coefs[1])+self.y+self.size], fill=random.choice(self.colors))      
            self.draw.rectangle([-self.xpoly+self.x, self.ypoly(self.coefs[2])+self.y, 
                -self.xpoly+self.x+self.size, self.ypoly(self.coefs[2])+self.y+self.size], fill=random.choice(self.colors))    
            self.draw.rectangle([-self.xpoly+self.x, self.ypoly(self.coefs[3])+self.y, 
                -self.xpoly+self.x+self.size, self.ypoly(self.coefs[3])+self.y+self.size], fill=random.choice(self.colors))     
            self.draw.rectangle([-0.5*self.xpoly+self.x, self.ypoly(self.coefs[4])+self.y, 
                -0.5*self.xpoly+self.x+self.size, self.ypoly(self.coefs[4])+self.y+self.size], fill=random.choice(self.colors)) 

            # Give the fireworks an "aura"
            self.blur = self.img.filter(ImageFilter.GaussianBlur(radius=10))
            self.output = ImageChops.lighter(self.img, self.blur)
            yield self.output

num_offireworks = 10
gif = []

for x in range(num_offireworks):
    animation = Animation(5)
    gif.extend(list(chain(animation.create_decoration(), animation.main())))

if __name__ == '__main__':
    gif[0].save('Desktop/test.gif',
        save_all=True, append_images=gif, optimize=False, duration=50, loop=0)