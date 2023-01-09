def encodeBinary(text: str, preserveWhitespaceInLetters=''):
    binary = preserveWhitespaceInLetters.join(bin(ord(i))[2:] for i in text)
    return binary

def decodeBinary(binary: str):
    eachBinarySub = ""
    stop = False
    text = ""
    for i in range(0, len(binary)):
        if binary[i].isspace() or stop:
            # decode binary here
            text += chr(int(eachBinarySub, base=2))
            eachBinarySub = ""
            continue
        elif i+1 == len(binary)-1:
            eachBinarySub += binary[i:]
            stop = True
        else:
            eachBinarySub += binary[i]
    
    return text

def main():
    while True:
        string = input("Enter string : ")
        status = input("Encode or Decode : ").lower()
        if status == "encode":
            preserveWhitespace = input("Do you want whitespace b/w letters (yes/no) : ").lower()
            if preserveWhitespace == "yes":
                preserveWhitespace = " "
                print(encodeBinary(string, preserveWhitespace))
            else:
                print(encodeBinary(string))
        elif status == "decode":
            print(decodeBinary(string))
        else:
            raise Exception("Status can contain only two values \"Encode\" or \"Decode\"")

main()
