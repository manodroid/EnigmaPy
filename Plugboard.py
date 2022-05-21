class Plugboard:

    def __init__(self, pairs):
        self.left = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.right = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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