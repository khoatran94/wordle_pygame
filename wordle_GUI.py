import pygame
import string
import operator
from itertools import compress
from word_helper import pick_word, check_word
from pygame_vkeyboard import *
from button_creator import Button

pygame.init()

class Wordle():

    # window margins
    WINDOW_SIZE = (800, 1000)
    MARGIN = 10
    TOP = 100
    BOTTOM = 100
    LR = 200

    #colors
    GREY = (128,128,128)
    DARK_GREY = (50,50,50)
    GREEN = (34,139,34)
    YELLOW =(175,175,0)
    BLACK =(0,0,0)
    WHITE = (200,200,200)
    ALPHABET = string.ascii_lowercase


    def __init__(self, word_length=5):


        #gameplay parameters
        self.true_word = pick_word(word_length)
        self.guesses = [[' ']*word_length for _ in range(6)]
        self.guesses_colors = [[Wordle.GREY]*word_length for _ in range(6)]
        self.lives = 0
        self.pos = 0
        self.endgame_message = 'Use keyboard or buttons to guess'
        self.gameplay_message = ''
        self.endgame = False
        self.win = False

        #display parameters
        self.SQ_size = (Wordle.WINDOW_SIZE[0]-(word_length-1)*Wordle.MARGIN-2*Wordle.LR) // word_length

        self.game_window = pygame.display.set_mode(Wordle.WINDOW_SIZE)

        self.FONT = pygame.font.SysFont('free sans bold',self.SQ_size)
        self.FONT_small = pygame.font.SysFont('arial',30)

    

    def draw(self):
        message_display = self.FONT_small.render(self.endgame_message , False, Wordle.WHITE)
        surf = message_display.get_rect(center = (Wordle.WINDOW_SIZE[0]//2, Wordle.TOP//2))
        self.game_window.blit(message_display, surf)
        
        message_display = self.FONT_small.render(self.gameplay_message , False, Wordle.WHITE)
        surf = message_display.get_rect(center = (Wordle.WINDOW_SIZE[0]//2, Wordle.TOP+6*self.SQ_size+5*Wordle.MARGIN+45))
        self.game_window.blit(message_display, surf)


        y = Wordle.TOP
        for i in range(6):
            x = Wordle.LR
            for j in range(len(self.true_word)):
                square = pygame.Rect(x,y, self.SQ_size, self.SQ_size)
                if i<self.lives:
                    pygame.draw.rect(self.game_window, self.guesses_colors[i][j], square, 0)
                else:
                    pygame.draw.rect(self.game_window, self.guesses_colors[i][j], square, 2)
            
                letter = self.FONT.render(self.guesses[i][j].upper(), False, Wordle.WHITE)
                surf = letter.get_rect(center = (x+self.SQ_size//2,y+self.SQ_size//2))
                self.game_window.blit(letter, surf)

                x += (self.SQ_size+Wordle.MARGIN)
            y += (self.SQ_size+Wordle.MARGIN)


    def guess_word(self, user_word):

        colors = [Wordle.GREY]*len(user_word)

        mask = list(map(operator.eq, user_word, self.true_word ))
        true_word_remaining = list(compress(self.true_word, [not i for i in mask]))

        for i, letter in enumerate(user_word):
            if mask[i]:
                colors[i] = Wordle.GREEN
            elif letter in true_word_remaining:
                colors[i] = Wordle.YELLOW
                true_word_remaining.remove(letter)
            else:
                colors[i] = Wordle.DARK_GREY
        return colors


if __name__ == '__main__':

    user_input = input('please type in 1 of 3 options: 5, 6, 7, for the length of the word ')
    
    while user_input not in ['5', '6', '7']:
        user_input = input('wrong mode, please choose one of 3 options: 5, 6, 7, for the length of the word ')

    wordle = Wordle(int(user_input))


    #virtual keyboard layout and graphical paramerters
    keyboard_layout = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
            [(3,'return'), (4,'space'), (3,'backspace')]]
    alphabet_letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
            'z', 'x', 'c', 'v', 'b', 'n', 'm']
    LR = 50
    button_size = (Wordle.WINDOW_SIZE[0]-2*LR-9*Wordle.MARGIN)//10
    #initialize buttons to create a virtual keyboard
    keyboard = []
    y = 700
    for i in range(3):
        number_of_keys = len(keyboard_layout[i])
        x =  (Wordle.WINDOW_SIZE[0] - number_of_keys*button_size - (number_of_keys-1)*Wordle.MARGIN)//2
        for j in range(len(keyboard_layout[i])):
            button = Button(x,y, button_size, button_size, text=keyboard_layout[i][j])
            keyboard.append(button)
            x += (button_size+Wordle.MARGIN)
        y += (button_size+Wordle.MARGIN)

    x =  (Wordle.WINDOW_SIZE[0] - len(keyboard_layout[0])*button_size - (len(keyboard_layout[0])-1)*Wordle.MARGIN)//2
    for i, letter in keyboard_layout[3]:
        x_size = i*button_size+(i-1)*Wordle.MARGIN
        button = Button(x,y, x_size, button_size, letter)
        keyboard.append(button)
        x += x_size+Wordle.MARGIN





    run = True
    while run:

        timer = pygame.time.Clock()
        timer.tick(20)
        wordle.game_window.fill(Wordle.BLACK)
        wordle.draw()

        for button in keyboard:
            button.draw(wordle.game_window)
        #listen for events in pygame (pygame.events)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.TEXTINPUT and wordle.pos<len(wordle.true_word) and not wordle.endgame:
                entry = event.__getattribute__('text').lower()
                if entry in Wordle.ALPHABET:
                        wordle.guesses[wordle.lives][wordle.pos] = entry
                        wordle.pos += 1 
                else:
                        wordle.gameplay_message = 'Only alphabetical letters allowed!'
                
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE and wordle.pos > 0:
                        wordle.guesses[wordle.lives][wordle.pos-1] = ' '
                        wordle.pos -= 1
                    if event.key == pygame.K_RETURN and not wordle.endgame:
                        if wordle.pos == len(wordle.true_word):
                            user_word = ''.join(wordle.guesses[wordle.lives])
                            if check_word(user_word):
                                colors = wordle.guess_word(user_word)
                                wordle.guesses_colors[wordle.lives] = colors
                                for color, letter in zip(colors, user_word):
                                    index = alphabet_letters.index(letter)
                                    if keyboard[index].get_color() == Wordle.GREEN:
                                        pass
                                    else:
                                        keyboard[index].set_color(color)
                                if user_word == wordle.true_word:
                                    wordle.win = True

                                wordle.pos = 0
                                wordle.lives += 1
                            else:
                                wordle.gameplay_message = "Please enter a meaningful word"
                        else:
                            wordle.gameplay_message = "Please fill the word before submitting"
                    if event.key == pygame.K_SPACE and wordle.endgame:
                        wordle.__init__()
                        for button in keyboard:
                            button.set_color(Wordle.GREY)
                        break

            if wordle.lives == 6:
                if not wordle.win:
                    wordle.endgame_message = "You lost!!! The word is {}".format(wordle.true_word.upper())
                    wordle.gameplay_message = "Press SPACE to start new game"
                    wordle.endgame = True
                else:
                    wordle.endgame_message  = 'Congratulations, you won!!!'
                    wordle.gameplay_message = "Press SPACE to start new game"
                    wordle.endgame = True

            elif wordle.win:
                wordle.endgame =True
                wordle.endgame_message  = 'Congratulations, you won!!!'
                wordle.gameplay_message = "Press SPACE to start new game"
                
        pygame.display.flip()
    pygame.quit()