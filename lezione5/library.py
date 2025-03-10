class Particle:
    def __init__(self, x, y, vx, vy, radius, colour):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy 
        self.radius = radius
        self.colour = colour 
        self.mass = self.radius ** 2
    
    def move(self, dt):
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt

    def draw(self, canvas):
        canvas.fill_style = self.colour
        canvas.fill_circle(self.x, self.y, self.radius)