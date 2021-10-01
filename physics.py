from math import cos, sin, pi, sqrt 
from random import randrange

class particle:

    g = 9.8
    dt = .2

    def __init__(self, radius, width, height, x, y):
        self.width, self.height = width, height
        self.radius = radius
        self.x, self.y = (x, y)
        self.vx, self.vy = (0, 0)
        self.color = self.random_color()
        self.collision_list = []

    def random_color(self):
        r = randrange(0, 255)
        g = randrange(0, 120)
        b = randrange(0, 255)
        return (r, g, b)

    def move(self):
        self.vy += self.g*self.dt
        self.y += self.vy*self.dt
        self.x += self.vx*self.dt

        # wall collisions 
        if(self.y + self.radius > self.height): 
            self.y = self.height - self.radius
            self.vy = -self.vy
        if(self.y - self.radius < 0):
            self.vy = -self.vy
            self.y = 0 + self.radius 
        if(self.x + self.radius > self.width):
            self.x = self.width - self.radius
            self.vx = -self.vx
        if(self.x - self.radius < 0):
            self.x = 0 + self.radius
            self.vx = -self.vx

        # 2D elastic collision
        for particle in self.collision_list:
            if self.distance(particle) <= 0:
                self.collide(particle)

    def collide(self, particle):
        pass

    def distance(self, particle):
        x1, y1 = self.x, self.y
        x2, y2 = particle.x, particle.y 
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def calculuate_collision(self, x1, y1, x2, y2):
        v1
        num = v1*cos(ma1-ca)*(m1-m2) + 2*m2*v2*cos(ma2-ca)
        return num

    def movement_angle(self, particle):
        return 0

    def contanct_angle(self, particle):
        return 0

    def magnitude(self, particle):
        return 0

#     @staticmethod
#     def contact_angle(a, b):
        

    def getpos(self):
        return (round(self.x), round(self.y))

