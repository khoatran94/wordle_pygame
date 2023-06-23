import pygame
import string


pygame.init()
#margins
WINDOW_SIZE = (800, 1000)
MARGIN = 10
TOP = 100
BOTTOM = 50
LR = 50

#colors
GREY = [128,128,128]
GREEN = (34,139,34)
YELLOW =(175,175,0)
BLACK =(0,0,0)
WHITE = (200,200,200)

ALPHABET = string.ascii_lowercase

FONT = pygame.font.SysFont('free sans bold',50)
FONT_small = pygame.font.SysFont('free sans bold', 30)



class Button():
    def __init__(self, x, y, width, height, text=''):

        button_surface = pygame.Surface((width, height))
        self.rect = button_surface.get_rect(topleft=(x,y))
        self.clicked = False
        self.parameter = (x,y,width,height)
        self.color = (128,128,128)
        self.text = text

    def draw(self, surface):

        pygame.draw.rect(surface, self.color, self.parameter, 0, border_radius=5)
        if self.text in ALPHABET:

            letter  = FONT.render(self.text.upper(), False, WHITE)
        elif self.text == 'space':
            letter  = FONT_small.render(self.text.upper(), False, WHITE)
        elif self.text == 'return':
            letter  = FONT_small.render('enter'.upper(), False, WHITE)
        else:
            letter  = FONT_small.render('backspace'.upper(), False, WHITE)
        surf = letter.get_rect(center=(self.rect[0]+self.rect[2]//2, self.rect[1]+self.rect[3]//2))
        surface.blit(letter, surf)

        pos = pygame.mouse.get_pos()

        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                if self.text in ALPHABET:
                    action = pygame.event.Event(pygame.TEXTINPUT, key = pygame.key.key_code(self.text), text=self.text)
                    pygame.event.post(action)
                else:
                    action = pygame.event.Event(pygame.KEYDOWN, key = pygame.key.key_code(self.text))
                    pygame.event.post(action)

        if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
    def set_color(self, color):
        self.color = color
    def get_color(self):
        return self.color

if __name__ == '__main__':

    keyboard_layout = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
            ['return', 'space', 'backspace']]



    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Button Demo')
    keyboard = []


    sq_size = (WINDOW_SIZE[0]-2*LR-6*MARGIN)//7
    enter_button = Button(LR, WINDOW_SIZE[1]-BOTTOM-sq_size, 2*sq_size+MARGIN, sq_size, 'return')
    space_button = Button(LR+2*sq_size+2*MARGIN, WINDOW_SIZE[1]-BOTTOM-sq_size, 3*sq_size+2*MARGIN, sq_size, 'space')
    backspace_button = Button(LR+5*sq_size+5*MARGIN, WINDOW_SIZE[1]-BOTTOM-sq_size, 2*sq_size+MARGIN, sq_size, 'backspace')
    keyboard.append(enter_button)

    run = True
    while run:

        screen.fill((255,255,255))
        enter_button.draw(screen)
        space_button.draw(screen)
        backspace_button.draw(screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print('enter')
                if event.key == pygame.K_SPACE:
                    print('space')
                if event.key == pygame.K_BACKSPACE:
                    print('backspace')
            if event.type == pygame.TEXTINPUT:
                entry = event.__getattribute__('text')
                print(entry)   

        pygame.display.flip()

    pygame.quit()