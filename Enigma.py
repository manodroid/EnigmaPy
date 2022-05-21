class Enigma:

    def __init__(self, re, rotors: list, pb, kb):
        self.re = re
        self.rotors = rotors
        self.pb = pb
        self.kb = kb

    def inward(self, letter):
        """the return from keyboard through all rotors"""
        return -1

    def backward(self, letter):
        """the return from the reflector and all rotors"""
        return -1

    def set_rings(self, rings):
        for rotor, ring in zip(self.rotors, rings):
            rotor.setRing(ring)

    def set_key(self, keys):
        for rotor, key in zip(self.rotors, keys):
            rotor.rotateToLetter(key)

    # try to remove keyboard plug board and maybe reflector
    def encipher(self, text):
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

        # remove this to their own functions
            signal = self.kb.forward(letter)
            signal = self.pb.forward(signal)
            signal = self.rotors[2].forward(signal)
            signal = self.rotors[1].forward(signal)
            signal = self.rotors[0].forward(signal)
            signal = self.re.reflect(signal)
            signal = self.rotors[0].backward(signal)
            signal = self.rotors[1].backward(signal)
            signal = self.rotors[2].backward(signal)
            signal = self.pb.backward(signal)
            res += self.kb.backward(signal)
        return res
