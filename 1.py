import sys, pygame, time


class Ball:
    def __init__(self, rect):
        self.rect = rect
        self.rect = self.rect.move(width / 2, height / 2)
        self.v = [0, 0]
        self.a = [0, 0]
        self.f = [0, 0]

    def move(self):
        t = 1
        d = [self.v[0] + (self.a[0] + self.f[0]) / 2 * t * t, self.v[1] + (self.a[1] + self.f[1]) / 2 * t * t]
        # print(self.rect)
        self.rect = self.rect.move(d)
        self.v[0] += (self.a[0] + self.f[0]) * t
        self.v[1] += (self.a[1] + self.f[1]) * t
        if self.rect.left <= 0 and self.v[0] < 0 or self.rect.right >= width and self.v[0] > 0:
            self.v[0] = -self.v[0]
        if self.rect.top <= 0 and self.v[1] < 0 or self.rect.bottom >= height and self.v[1] > 0:
            self.v[1] = -self.v[1]


pygame.init()

size = width, height = 1900, 1000

black = 0, 0, 0

screen = pygame.display.set_mode(size)

pic = pygame.image.load("ball.gif")

ball = Ball(pic.get_rect())

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    lastrect = ball.rect

    keys = pygame.key.get_pressed()
    mousepos = pygame.mouse.get_pos()

    for i in range(1):
        ball.f = [-ball.v[0] / 40, -ball.v[1] / 40]
        # ball.f = [0, 0]

        if keys[pygame.K_UP]:
            ball.f[1] -= 10
        if keys[pygame.K_DOWN]:
            ball.f[1] += 10
        if keys[pygame.K_LEFT]:
            ball.f[0] -= 10
        if keys[pygame.K_RIGHT]:
            ball.f[0] += 10

        ball.f[0] += (mousepos[0] - ball.rect.center[0]) / 100
        ball.f[1] += (mousepos[1] - ball.rect.center[1]) / 100

        ball.move()

    screen.fill(black)
    screen.blit(pic, ball.rect)
    # print(ball.rect, lastrect)
    pygame.display.update([lastrect, ball.rect])
    time.sleep(0.04)
