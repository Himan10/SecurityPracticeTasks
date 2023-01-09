# Encode/Decode morse code

from json import load

def solveCipher(text, status):

    with open("morse-code.json", 'r') as file:
        morseCodeDict = load(file)

    def encodeStringToMorseCode(text: str):
        morsecode = ""
        for i in range(0, len(text)):
            if text[i].isspace():
                morsecode += ' / '
                continue
            else:
                if text[i] in morseCodeDict:
                    morsecode += morseCodeDict[text[i]]
                    morsecode += ' '

        return morsecode

    def decodeMorseCodeToString(morsecode: str):
        text = ""
        morsecodeList = morsecode.split(' / ')
        for morsecodesub in morsecodeList:
            subMorseCodeList = morsecodesub.split(" ")
            for eachMorseCodeString in subMorseCodeList:
                for eachItem in morseCodeDict.items():
                    if eachItem[1] == eachMorseCodeString:
                        text += eachItem[0]
                        break
            text += " "

        return text


    if status == "encode":
        print(encodeStringToMorseCode(text.lower()))
    elif status == "decode":
        print(decodeMorseCodeToString(text.lower()))
    else:
        raise Exception("status can contain only two values \"Encode\" & \"Decode\"")

def main():
    while True:
        string = input("Enter String : ")
        status = input("You want to encode or decode : ")
        solveCipher(string, status)
