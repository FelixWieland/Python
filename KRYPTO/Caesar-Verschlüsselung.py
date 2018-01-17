#Caesar-Verschlüsselung
import os

class Caesar:
    abc_k = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    abc_g = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    def remove_whitespace(self, text):
        text_without_whitespace = []
        for pos in range(len(text)):
            if text[pos] == " ":
                continue
            else:
                text_without_whitespace.append(text[pos])
        return ''.join(text_without_whitespace)

    def encode(self, text, key):
        encoded = []
        text_without_whitespace = self.remove_whitespace(text)
        for pos in range(len(text_without_whitespace)):
            for integer, string in enumerate(self.abc_k):
                if string == text_without_whitespace[pos]:
                    encoded.append(self.abc_k[integer - key])
                if self.abc_g[integer] == text_without_whitespace[pos]:
                    encoded.append(self.abc_g[integer - key])
        return ''.join(encoded)

    def decode(self, text, key="default"):
        if key == "default":
            for key in range(25):
                decoded = []
                text_without_whitespace = self.remove_whitespace(text)
                key = key*(-1)
                for pos in range(len(text_without_whitespace)):
                    for integer, string in enumerate(self.abc_k):
                        if string == text_without_whitespace[pos]:
                            value = integer - key
                            if value > 25:
                                value = value-len(self.abc_k)
                            decoded.append(self.abc_k[value])
                        if self.abc_g[integer] == text_without_whitespace[pos]:
                            value = integer - key
                            if value > 25:
                                value = value-len(self.abc_g)
                            decoded.append(self.abc_g[value])
                print("Key="+ str(key) + " " + ''.join(decoded))
        else:
            decoded = []
            text_without_whitespace = self.remove_whitespace(text)
            key = key*(-1)
            for pos in range(len(text_without_whitespace)):
                for integer, string in enumerate(self.abc_k):
                    if string == text_without_whitespace[pos]:
                        value = integer - key
                        if value > 25:
                            value = value-len(self.abc_k)
                        decoded.append(self.abc_k[value])
                    if self.abc_g[integer] == text_without_whitespace[pos]:
                        value = integer - key
                        if value > 25:
                            value = value-len(self.abc_g)
                        decoded.append(self.abc_g[value])
            return ''.join(decoded)

if __name__ == '__main__':
    cs = Caesar()
    print("Ceasar-Verschlüsselung")
    print("Version: 1.0")
    print("")
    text = input("Geben Sie einen Text zum verschlüsseln ein: ")
    key = int(input("Geben Sie den gewünschten Schlüssel ein (gerade Zahl von 0-26): "))
    print("")
    print("Verschlüsselter Text:" + cs.encode(text, key))
    print("")
    answer = input("Wollen sie den selben Text entschlüsseln? (y/n): ")
    if answer == "y":
        print("")
        print("Enschlüsselter Text: " + cs.decode(cs.encode(text, key), key))
    else:
        answer = input("Wollen sie einen anderen Text entschlüsseln? (y/n): ")
        if answer == "y":
            text = input("Geben Sie einen Text zum entschlüsseln ein: ")
            key = input("Geben Sie einen Schlüssel zum entschlüsseln ein: ")
            if key == "":
                print("")
                print("Versuche Key zu knacken, moegliche Keys:")
                print("")
                print(cs.decode(text))
            else:
                print("")
                print("Enschlüsselter Text: " + cs.decode(text, int(key)))
