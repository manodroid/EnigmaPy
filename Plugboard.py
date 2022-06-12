import pygame
ALPA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Plugboard:

    def __init__(self, pairs):
        self.left = ALPA
        self.right = ALPA
        for pair in pairs:
            A, B = pair[0], pair[1]
            posA, posB= self.left.find(A), self.left.find(B)
            self.left = self.left[:posA] + B + self.left[posA+1:]
            self.left = self.left[:posB] + A + self.left[posB+1:]

    def forward(self, signal):
        letter = self.right[signal]
        return self.left.find(letter)

    def backward(self, signal):
        letter = self.left[signal]
        return self.right.find(letter)

    def draw(self, screen, x, y, w, h, font):
        #rectangle
        r = pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen, "white", r, width=2, border_radius=15)

        for i in range(26):
            letter = self.left[i] # left hand side
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center = (x+w/4, y+(i+1)*h/27))
            screen.blit(letter, text_box)

            letter = self.right[i] # right hand side
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center = (x+w*3/4, y+(i+1)*h/27))
            screen.blit(letter, text_box)

            
