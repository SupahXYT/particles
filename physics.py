from random import randrange

class particle:

    g = 0
    dt = .2
    f = 1

    def __init__(self, mass, width, height, x, y):
        self.width, self.height = width, height
        self.radius = mass
        if mass > 90:
            self.mass = mass*10
        else:
            self.mass = mass
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

        # 2D elastic collision
        for particle in self.collision_list:
            if self.distance_squared(particle) <= (self.radius + particle.radius)**2:
                self.collide(particle)

        # wall collisions 
        # if(self.y + self.radius > self.height): 
        #     self.y = self.height - self.radius
        #     self.vy = -self.f*self.vy
        #     self.vx = self.f*self.vx
        # if(self.y - self.radius < 0):
        #     self.y = 0 + self.radius 
        #     self.vy = -self.f*self.vy
        #     self.vx = self.f*self.vx
        # if(self.x + self.radius > self.width):
        #     self.x = self.width - self.radius
        #     self.vx = -self.f*self.vx
        #     self.vy = self.f*self.vy
        # if(self.x - self.radius < 0):
        #     self.x = 0 + self.radius
        #     self.vx = -self.f*self.vx
        #     self.vy = self.f*self.vy

        self.vy += self.g*self.dt
        self.y += self.vy*self.dt
        self.x += self.vx*self.dt

    def distance_squared(self, particle):
        x1, y1 = self.x, self.y
        x2, y2 = particle.x, particle.y 
        return (x2 - x1)**2 + (y2 - y1)**2
    
    def collide(self, particle):
        distx = self.x - particle.x
        disty = self.y - particle.y
        vx = particle.vx - self.vx
        vy = particle.vy - self.vy
        dot_product = distx*vx + disty*vy

        if dot_product > 0:
            scale = dot_product / (distx**2 + disty**2)
            xcol = distx * scale
            ycol = disty * scale

            mass_sum = self.mass + particle.mass
            col_weight_self = 2*particle.mass / mass_sum
            col_weight_particle = 2*self.mass / mass_sum 
            self.vx += col_weight_self * xcol
            self.vy += col_weight_self * ycol
            particle.vx -= self.f*col_weight_particle * xcol
            particle.vy -= self.f*col_weight_particle * ycol

    def update_col_list(self, list):
        self.collision_list= []
        for particle in list:
            if(self is not particle):
                self.collision_list.append(particle)

    def other_lines(self):
        lines = []
        for particle in self.collision_list:
            lines.append((self.x, self.y))
            lines.append((particle.x, particle.y))
        return lines

    def getpos(self):
        return (round(self.x), round(self.y))

