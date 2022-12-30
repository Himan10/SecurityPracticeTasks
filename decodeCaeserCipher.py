# This is the 1st question mentioned in task2Details

import json
import pprint

class SolveCiphers():

    def __init__(self, cipherName=None):
        self.cipherName = cipherName
        with open("words_dictionary.json", 'r') as fp:
            self.wordsDict = json.load(fp)


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
           
            if letter.isspace():
                return " "
            if letter.islower():
                return doStuff2(97, 122) # for lower letters
            else:
                return doStuff2(65, 90) # for upper letters

        encodedInput = input("Enter encoded input : ")
        shiftKey = 0
        shiftKeyLimit = 0
        result = {}
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
            for i in range(len(encodedInput)):
                string += doStuff(encodedInput[i], shiftKey)
                if (encodedInput[i].isspace() or i == len(encodedInput)-1):
                    # find out the existence of a word
                    word = string.split()[-1].lower()
                    result[word] = self.wordsDict.get(word, 0)
            print(string, result)

        elif shiftKeyLimit:
            for key in range(1, shiftKeyLimit+1):
                string = ""
                total = 0
                for i in range(len(encodedInput)):
                    string += doStuff(encodedInput[i], key)
                    if (encodedInput[i].isspace() or i == len(encodedInput)-1):
                        word = string.split()[-1].lower()
                        total += self.wordsDict.get(word, 0)

                result[string] = total

        print("Matched Results\t\t String\t\t Shift Key\n")
        for i, item in enumerate(result.items()):
            print(f"{item[1]}\t\t {item[0]}\t\t {i+1}")
