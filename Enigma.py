class Enigma:

    def __init__(self, re, rotors: list, pb, kb):
        self.re = re
        self.rotors = rotors
        self.pb = pb
        self.kb = kb

    def set_rings(self, rings):
        for rotor, ring in zip(self.rotors, rings):
            rotor.setRing(ring)

    def set_key(self, keys):
        for rotor, key in zip(self.rotors, keys):
            rotor.rotateToLetter(key)

    def encipher(self, letter):
        r1, r2, r3 = self.rotors
        if r2.left[0] == r2.notch and r3.left[0] == r3.notch:
            r1.rotate()
            r2.rotate()
            r3.rotate()
        elif r2.left[0] == r2.notch:
            r1.rotate()
            r2.rotate()
            r3.rotate()
        elif r3.left[0] == r3.notch:
            r2.rotate()
            r3.rotate()
        else:
            r3.rotate()

        # add option to skip backspace and space
        signal = self.kb.forward(letter)
        path = [signal, signal]
        signal = self.pb.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = r3.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = r2.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = r1.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.re.reflect(signal)
        path.append(signal)
        path.append(signal)
        path.append(signal)
        signal = r1.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = r2.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = r3.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.pb.backward(signal)
        path.append(signal)
        path.append(signal)
        letter = self.kb.backward(signal)
        return path, letter
