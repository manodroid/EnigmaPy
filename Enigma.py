class Enigma:

    def __init__(self, re, rotors: list, pb, kb):
        self.re = re
        self.rotors = rotors
        self.pb = pb
        self.kb = kb

    def inward(self, letter):
        """the return from keyboard through all rotors"""
        signal = self.kb.forward(letter)
        signal = self.pb.forward(signal)
        for r in self.rotors[::-1]:
            signal = r.forward(signal)
        return signal

    def backward(self, letter):
        """the return from the reflector and all rotors"""
        signal = letter
        for r in self.rotors:
            signal = r.backward(signal)
        signal = self.pb.backward(signal)
        return self.kb.backward(signal)

    def set_rings(self, rings):
        for rotor, ring in zip(self.rotors, rings):
            rotor.setRing(ring)

    def set_key(self, keys):
        for rotor, key in zip(self.rotors, keys):
            rotor.rotateToLetter(key)

    def encipher(self, text: object) -> object:
        res = ''
        for letter in text:
            if letter == " ":
                res += ' '
                continue
            self.rotors[2].rotate()
            if self.rotors[2].left[0] == self.rotors[2].notch:  # second rotor shifts every 26 letters
                self.rotors[1].rotate()
            elif self.rotors[1].left[0] == self.rotors[1].notch:  # third rotor shifts every 26^2 letters
                self.rotors[0].rotate()

            signal = self.inward(letter)  # input from rotors
            signal = self.re.reflect(signal)  # reflector output
            res += self.backward(signal)  # output from reflectors
        return res
