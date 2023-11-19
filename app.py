import pygame


class Ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self, window):
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), 5)


class Club:
    def __init__(self):
        self.frames = []
        self.frame_index = 0
        self.frame_delay = 10
        self.frame_counter = 0
        self.is_hitting = False

    def load_animation(self, frame_filenames):
        for filename in frame_filenames:
            frame = pygame.image.load(filename)
            self.frames.append(frame)

    def update(self):
        if self.is_hitting:
            self.frame_counter += 1
            if self.frame_counter >= self.frame_delay:
                self.frame_index += 1
                if self.frame_index >= len(self.frames):
                    self.frame_index = 0
                self.frame_counter = 0

    def draw(self, window):
        if self.is_hitting:
            frame = self.frames[self.frame_index]
            window.blit(frame, (320, 620))


class Course:
    def __init__(self):
        self.image = pygame.image.load("./course.png").convert_alpha()

    def update(self):
        pass

    def draw(self, window):
        window.blit(self.image, (0, 0))


pygame.init()


window_width = 1000
window_height = 700
window_size = (window_width, window_height)

window = pygame.display.set_mode(window_size)
pygame.display.set_caption("2D Golf")

ball = Ball(413,660)
club = Club()
course = Course()

club.load_animation(["./club.png",
                    "./club2.png",
                    "./club3.png",
                    "./club4.png"])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and not club.is_hitting:
        club.is_hitting = True

    ball.update()
    club.update()
    course.update()
    # Add game logic and drawing here

    window.fill((0, 255, 0))
    course.draw(window)
    ball.draw(window)
    club.draw(window)
    pygame.display.update()

pygame.quit()