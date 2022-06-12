import pygame


class Reflector:
    def __init__(self, wiring):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring

    def reflect(self, signal):
        letter = self.right[signal]
        return self.left.find(letter)

    def draw(self, screen, x, y, w, h, font):
        """Renders the rotor through pygame"""
        # rectangle
        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "white", r, width=2, border_radius=15)

        for i in range(26):
            letter = self.left[i]  # left hand side
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center=(x + w / 4, y + (i + 1) * h / 27))
            screen.blit(letter, text_box)

            if i == 0:  # highlight top letter
                pygame.draw.rect(screen, "teal", text_box, border_radius=5)

            screen.blit(letter, text_box)

            letter = self.right[i]  # right hand side
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center=(x + w * 3 / 4, y + (i + 1) * h / 27))
            screen.blit(letter, text_box)
