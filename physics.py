from math import cos, sin, pi, sqrt 
from random import randrange

class particle:

    g = 9.8
    dt = .2

    def __init__(self, radius, width, height, x, y):
        self.width, self.height = width, height
        self.radius = radius
        self.mass = 1
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

    def distance(self, particle):
        x1, y1 = self.x, self.y
        x2, y2 = particle.x, particle.y 
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def collide(self, particle):
        v1 = self.scalar_size(self)
        v2 = self.scalar_size(particle)
        ma1 = self.movement_angle(self)
        ma2 = self.movement_angle(particle)
        ca = self.contanct_angle(particle)
        ms1 = self.mass
        ms2 = particle.mass
        self.vx, self.vy = self.calculate_collision(v1, v2, ma1, ma2, ca, ms1, ms2)
        particle.vx, self.vy = self.calculate_collision(v2, v1, ma2, ma1, ca, ms2, ms1)

    def calculate_collision(self, v1, v2, ma1, ma2, ca, ms1, ms2):
        num = v1*cos(ma1 - ca)*(ms1 - ms2) + 2*ms2*v2*cos(ma2 - ca)
        den = ms1+ms2
        fx_side = cos(ca)+v1*sin(ma1-ca)*cos(ca+pi/2)
        fy_side = sin(ca)+v1*sin(ma1-ca)*sin(ca+pi/2)
        return ((num/den)*fx_side, (num/den)*fy_side)

    def movement_angle(self, particle):
        return 0

    def contanct_angle(self, particle):
        return 0

    def scalar_size(self, particle):
        return 0

    def getpos(self):
        return (round(self.x), round(self.y))

