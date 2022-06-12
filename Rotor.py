import pygame
ALPA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Rotor:

    def __init__(self, wiring, notch):
        self.left = ALPA
        self.right = wiring
        self.notch = notch

    def forward(self, signal):
        letter = self.right[signal]
        return self.left.find(letter)

    def backward(self, signal):
        letter = self.left[signal]
        return self.right.find(letter)

    def rotate(self, l=1, forward=True):
        for i in range(l):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[25] + self.left[:25]
                self.right = self.right[25] + self.right[:25]

    def setRing(self, ring):
        """rotate the rotor backward and adjust turnover notch to ring"""
        self.rotate(ring - 1, forward=False)
        notch = ALPA.find(self.notch)
        self.notch = ALPA[(notch - ring) % 26]

    def rotateToLetter(self, letter):
        """rotate rotor to a specific letter"""
        l = ALPA.find(letter)
        self.rotate(l)

    def draw(self, screen, x, y, w, h, font):
        """Renders the rotor through pygame"""
        #rectangle
        r = pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen, "white", r, width=2, border_radius=15)

        for i in range(26):
            letter = self.left[i] # left hand side
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center = (x+w/4, y+(i+1)*h/27))
            screen.blit(letter, text_box)

            if i == 0: # highlight top letter
                pygame.draw.rect(screen, "teal", text_box, border_radius=5) 

            if self.left[i] == self.notch: # highlight turnover notch
                letter = font.render(self.notch, True, "grey")
                pygame.draw.rect(screen, "white", text_box, border_radius=5) 

            screen.blit(letter, text_box)

            letter = self.right[i] # right hand side
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center = (x+w*3/4, y+(i+1)*h/27))
            screen.blit(letter, text_box)

