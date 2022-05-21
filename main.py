from Rotor import Rotor
from Reflector import Reflector
from Keyboard import Keyboard
from Plugboard import Plugboard
from Enigma import Enigma

# Rotors
I = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
II = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E')
III = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')
IV = Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J')
V = Rotor('VZBRGITYUPSDNHLXAWMJQOFECK', 'Z')
# Reflectors
A = Reflector('EJMZALYXVBWFCRQUONTSPIKHGD')
B = Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
C = Reflector('FVPJIAOYEDRZXWGCTKUQSBNMHL')
# Plug-KeyBoard
Kb = Keyboard()
P = Plugboard(['AR', 'Gk', 'OX'])

Enig = Enigma(A, [I, II, III], P, Kb)
Enig.set_key("MAN")
Enig.set_rings([1, 1, 1])

uin = input('Enter text you want to encipher -> ')
print(Enig.encipher(uin.upper()))