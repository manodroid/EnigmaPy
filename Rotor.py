class Rotor:

    def __init__(self, wiring, notch):
        self.left = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
        'rotate the rotor backward and adjust turnover notch to ring'
        self.rotate(ring-1, forward=False)
        notch = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(self.notch)
        self.notch = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[(notch-ring) % 26]


    def rotateToLetter(self, letter):
        'rotate rotor to a specific letter'
        l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(letter)
        self.rotate(l)