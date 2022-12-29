# This is the 1st question mentioned in task2Details

class SolveCiphers():

    def __init__(self, cipherName):
        self.cipherName = cipherName

    def caeserCipher(self):
        """Here the encryption on the string has already done before, 
        means, shift key has already been applied to the text for making it
        encrypted. This time, to decrypt the key, we will apply the shift
        key backwards to decrypt it.
        """
        def doStuff(letter, key):
            def doStuff2(initial, final):
                unicodeValueOfLetter = ord(letter)
                shiftKey = key
                while shiftKey > 0:
                    if unicodeValueOfLetter == initial:
                        unicodeValueOfLetter = final
                    else:
                        unicodeValueOfLetter -= 1
                    shiftKey -= 1
                return chr(unicodeValueOfLetter)
            
            if letter.islower():
                return doStuff2(97, 122)
            else:
                return doStuff2(65, 90) # for upper letters

        encodedInput = input("Enter encoded input : ")
        shiftKey = 0
        shiftKeyLimit = 0
        if not encodedInput:
            raise Exception("Empty value provided")
        try:
            shiftKey = int(input("Enter shift key value: "))
        except ValueError:
            print("Finding shift key for you")
            try:
                shiftKeyLimit = int(input("Enter shift key limit: "))
            except ValueError:
                raise Exception("Please Enter A Value Value")

        if shiftKey:
            string = ""
            for char in encodedInput:
                # lets consider it as all UPPERCASE
                if char.isspace():
                    string += char
                    continue
                string += doStuff(char, shiftKey)
            print(string)

        elif shiftKeyLimit:
            for key in range(1, shiftKeyLimit+1):
                string = ""
                for char in encodedInput:
                    if char.isspace():
                        string += char
                        continue
                    string += doStuff(char, key)
                print(string)
