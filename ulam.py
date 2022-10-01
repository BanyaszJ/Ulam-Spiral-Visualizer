from math import sqrt
from tkinter import font
import pygame
pygame.init()
# print("")
i = 0

class Main:
    def __init__(self) -> None:
        self.font_size = 0
        self.screen = Screen(w = 1000, h = 1000)
        self.ulam_generator = Ulam()

    def mainloop(self, font_size):
        stop = False
        self.font_size = font_size

        x = self.screen.get_width() / 2
        y = self.screen.get_height() / 2

        self.screen.fill()
        dir = 0
        curr_step = -1
        target_step = 1
        trigger = 0

        while not stop:            
            stop = self.screen.check_quit_pressed()
            if ((self.screen.get_height()*self.screen.get_width()) < (x*y)):
                continue

            self.ulam_generator.increment()
            if self.ulam_generator.isPrime():
                self.ulam_generator.set_curr_num_color("RED")
            else:
                self.ulam_generator.set_curr_num_color("BLACK")
                
            num = self.ulam_generator.get_curr_number()
            col = self.ulam_generator.get_curr_num_color()

            # self.screen.push_text(str(num), size=s, coords=(x, y), color = col)
            self.screen.push_text(str("X"), size=self.font_size, coords=(x, y), color = col)
            curr_step += 1

            if (curr_step == target_step):
                if dir < 3:
                    dir += 1
                elif (dir == 3): dir = 0 
                curr_step = 0

                trigger += 1
                if (trigger == 2):
                    target_step += 1
                    trigger = 0


            if (dir == 0): # right
                x += self.font_size
                y += 0
            elif (dir == 1): # up
                x += 0
                y -= self.font_size
            elif (dir == 2): # left
                x -= self.font_size
                y += 0
            elif (dir == 3): # down
                x -= 0
                y += self.font_size
            
            self.screen.update()
            self.screen.tick()


class Screen:
    def __init__(self, w = 0, h = 0) -> None:
        self._width     = w
        self._height    = h
        self._refresh_color = (0,0,0)

        self.frame  = pygame.display.set_mode((self._width, self._height))
        self.clock  = pygame.time.Clock()

        pygame.display.set_caption("Ulam spiral")

        self.text       = None
        self.textRect   = None

    def get_width(self):
        return self._width
        
    def get_height(self):
        return self._height

    def check_quit_pressed(self):
        quit_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_pressed = True

        return quit_pressed

    def push_text(self, txt_to_display = None, size = 0, coords = (), color = (0,0,0)):
        self.font        = pygame.font.Font('freesansbold.ttf', size)
        self.text        = self.font.render("X", True, color, color)

        self.frame.blit(self.text, coords)
        # pygame.draw.circle(self.frame, color, coords, size//2)

    def fill(self):
        self.frame.fill(self._refresh_color)

    def update(self):
        pygame.display.update()

    def tick(self, spd = 0):
        self.clock.tick(spd)


class Ulam:
    def __init__(self) -> None:
        # # self._primes = []
        self._dir = ["RIGHT", "UP", "LEFT", "DOWN"]
        self._curr_dir = 0

        self._curr_number = 0
        self._curr_number_color = (255,255,255)

    def get_curr_number(self):
        return self._curr_number

    def get_curr_num_color(self):
        return self._curr_number_color

    def set_curr_num_color(self, color):
        if color == "RED":
            self._curr_number_color = (255,0,0)
        elif color == "BLACK":
            self._curr_number_color = (255,255,255)
        else:
            print("Invalid color... defaulted to white")
            self._curr_number_color = (255,255,255)

    def set_curr_dir(self, dir):
        if dir not in [0,1,2,3]: dir = 0
        self._curr_dir = dir

    def get_curr_dir(self):
        return self._curr_dir

    def increment(self):
        self._curr_number += 1

    def isPrime(self):
        x = self._curr_number
        if (x == 2): return False
        for i in range(2, int(sqrt(x))+1):
            if (x % i == 0):
                return False

        return True


main    = Main()
main.mainloop(font_size = 2)
