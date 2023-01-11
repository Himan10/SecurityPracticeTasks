# Encode/Decode unicode strings

def encode(text):
    # According to the task, the format in which text is going to be encoded
    # is "%u0045", the prefix will be "%u" instead of `\u` followed by 4 hex digits
    encodedText = "".join("%u" + format(ord(i), "04x") for i in text)
    return encodedText

def decode(encodedText):
    text = ''.join(chr(int(encodedText[i: i+6][2:], base=16)) for i in range(0, len(encodedText), 6))
    return text   

def main():
    pass
