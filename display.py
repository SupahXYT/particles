import pygame, physics
import math

class Display():
    def __init__(self, width, height):
        pygame.init()
        self.display = pygame.display.set_mode((width, height))
        self.width, self.height = self.display.get_size()
        self.mass = 1
        self.particle_array = []
        pygame.display.flip()
        # self.particle_array.append(physics.particle(20, width, height, 200, 200))

    def main(self):
        self.draw()
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.on_click(event)
            self.draw()
            pygame.display.flip()
            pygame.time.wait(20)

        pygame.quit()        

    def draw(self):
        self.display.fill((0, 0, 0))
        for particle in self.particle_array:
            particle.move()
            pygame.draw.circle(self.display, particle.color, particle.getpos(), particle.radius)
            self.draw_vel_line(particle)

    def on_click(self, event):
        if event.button == 1:
            particle = physics.particle(50, self.width, self.height, event.pos[0], event.pos[1])
            self.particle_array.append(particle)
            for p in self.particle_array:
                p.update_col_list(self.particle_array)
            
        elif event.button == 3:
            particle = physics.particle(20, self.width, self.height, event.pos[0], event.pos[1])
            vx = physics.randrange(-30, 30)
            vy = physics.randrange(-30, 30)
            particle.vx, particle.vy = vx, vy
            self.particle_array.append(particle)
            for p in self.particle_array:
                p.update_col_list(self.particle_array)

    def draw_vel_line(self, particle):
        start = (particle.x, particle.y)
        end = (particle.x+particle.vx, particle.y+particle.vy)
        pygame.draw.line(self.display, (255, 255, 255), start, end)

    def draw_pull_line(self):
        # magnitude = math.sqrt((ex  - sx)**2 + (ey - sy)**2)
        pass

d = Display(800, 800)
d.main()
