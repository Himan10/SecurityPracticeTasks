# URL encoding works by converting each character into its ASCII value and then conver that value into HEX, and represent it using prefix %

def urlencoder(text: str):
    encodedmessage = ""
    for i in text:
        encodedmessage += "%" + hex(ord(i))[2:]

    print(encodedmessage)

def urldecoder(encodedtext: str):
    # check if captured hex value falls under
    # 0x00 - 0x8f or 0x90 - 0xff
    text = ""
    getHex = ""
    i = 0
    while i < len(encodedtext):
        if encodedtext[i] == "%":
            getHex += encodedtext[i:i+3]
            hex_ = "0x" + getHex[1:]
            decimalValueOfHex = int(hex_, base=16)
            # check if hex value falls under the correct hex encoding scheme
            if (int(decimalValueOfHex) in range(int(0x00), int(0x8f)+1) or
                int(decimalValueOfHex) in range(int(0x90), int(0xff)+1)):
                text += chr(decimalValueOfHex)
            else:
                print(text)
                text += hex_
            getHex = ""
            i += 2
        else:
            text += encodedtext[i]
        i += 1

    print(text)

def main():
    while True:
        string = input("Enter value : ")
        status = input("Encode or decode : ")
        if status == "encode":
            urlencoder(string)
        elif status == "decode":
            urldecoder(string)
        else:
            raise Exception("Value should either be \"encode\" or \"decode\"")

main()
