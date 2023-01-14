# Create sha1 of possible combinations from AAAA to ZZZZ
# sha1 has been cryptographically broken and there are many replacements of it. 

import hashlib
import sys

def printSHA1ofChars(data, fp):
    alphabets = ''.join(chr(i) for i in data)
    getSha = hashlib.sha1(alphabets.encode())
    if fp:
        fp.write(f"{alphabets}, {getSha.hexdigest()}\n")
        return
    print(alphabets, getSha.hexdigest())

def getCombinations(array, index):
    # This uses recursion but it can lead to MaxRecursionDepth Error or segmentation fault, although it works fine.
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

def getCombinationsAndPrintSHA():
    # Better function
    with open("output.txt", "w") as file:
        for i in range(65, 91):
            for j in range(65, 91):
                for k in range(65, 91):
                    for l in range(65, 91):
                        printSHA1ofChars([i, j, k, l], file)

    print("Output has been written to \"output.txt\"")

def main():
    data = [65, 65, 65, 65]
    #printSHA1ofChars(data)
    #getCombinations(data, len(data)-1)
    getCombinationsAndPrintSHA()
