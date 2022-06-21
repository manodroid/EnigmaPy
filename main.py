from Rotor import Rotor
from Reflector import Reflector
from Keyboard import Keyboard
from Plugboard import Plugboard
from Enigma import Enigma
from draw import draw

import pygame
from pygame.locals import *

# Gui setup
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma Simulator")
# fonts
ALPA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
print()
MONO = pygame.font.SysFont("De", 24)
BOLD = pygame.font.SysFont("FreeMono", 25, bold=True)
# global variables
WIDTH, HEIGHT = 1600, 900
MARGINS = {"top":200, "bottom":100, "left":100, "right":100}
GAP = 25
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
INPUT, OUTPUT = "", ""
PATH = []

# Rotors
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
# Reflectors
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
# Plug-KeyBoard
Kb = Keyboard()
P = Plugboard(["AR", "Gk", "OX"])

Enig = Enigma(A, [I, II, III], P, Kb)
Enig.set_key("MAN")
Enig.set_rings([1, 1, 1])


animating = True
while animating:

    SCREEN.fill("#333337")  # backgroung

    #text input
    text = BOLD.render(INPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2, MARGINS["top"]/2)) 
    SCREEN.blit(text, text_box)

    #text output
    text = MONO.render(OUTPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2, MARGINS["top"]/2+25)) 
    SCREEN.blit(text, text_box)
    
    # draw the enigma 
    draw(Enig,PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)
    pygame.display.flip()  # update the screen

    # track user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                III.rotate()
            elif event.key == pygame.K_SPACE:
                INPUT += " "
                OUTPUT += " "
            else:
                key = event.unicode
                if key in ALPA.lower():
                    INPUT += key.upper()
                    # update path error
                    PATH, cipher = Enig.encipher(key.upper())
                    OUTPUT += cipher
