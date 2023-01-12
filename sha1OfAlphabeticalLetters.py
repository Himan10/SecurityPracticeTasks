# Create sha1 of possible combinations from AAAA to ZZZZ
# sha1 has been cryptographically broken and there are many replacements of it. 

# Here, due to recursionLimit and SegmentationFault, I've restricted it to only 4 chars, from 'A' to 'D'
# Will fix soon

import hashlib
import sys

def printSHA1ofChars(data):
    alphabets = ''.join(chr(i) for i in data)
    getSha = hashlib.sha1(alphabets.encode())
    print(alphabets, getSha.hexdigest())

def getCombinations(array, index):
    if index > -1: 
        if index == len(array)-1:
            while array[index] != 68:
                array[index] += 1
                printSHA1ofChars(array)
            else:
                array[index] = 64
                getCombinations(array, index-1)
        else:
            array[index] += 1
            if array[index] > 68:
                array[index] = 64
                getCombinations(array, index-1)
            else:
                getCombinations(array, index+1)

    return

def main():
    data = [65, 65, 65, 65]
    printSHA1ofChars(data)
    getCombinations(data, len(data)-1)
