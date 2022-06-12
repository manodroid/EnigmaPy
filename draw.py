import pygame

def draw(enigma, path, screen, width, height, margins, gap, font):
    w = (width - margins["right"] - margins["left"] - 5*gap) / 6
    h = height - margins["top"] - margins["bottom"]
    r1, r2, r3 = enigma.rotors

    # path coordinates
    y = [margins["top"] + (signal + 1) * h/27 for signal in path]
    x = [width - margins["right"] - w / 2]
    for i in range(4, -1, -1):  # forward
        x.append(margins["left"] + i * (w + gap) + w * 3 / 4)
        x.append(margins["left"] + i * (w + gap) + w * 1 / 4)
    #x.append(width - margins["right"] + w *3/4)
    for i in range(1, 5):  # backward
        x.append(margins["left"] + i * (w + gap) + w * 1 / 4)
        x.append(margins["left"] + i * (w + gap) + w * 3 / 4)
    x.append(width - margins["right"] - w / 2)

    # draw path
    if len(path) > 0:
        for i in range(1, 20):
            if i < 10:
                color = "#43aa8b"
            elif i < 12:
                color = "#f9c74f"
            else:
                color = "#e63946"
            start = (x[i-1], y[i-1])
            end = (x[i], y[i])
            pygame.draw.line(screen, color, start, end, width=5)

    # component coordinates
    x, y = margins["left"], margins["top"]
    # enigma components
    for component in [enigma.re, r1, r2, r3, enigma.pb, enigma.kb]:
        component.draw(screen, x, y, w, h, font)
        x += w + gap
