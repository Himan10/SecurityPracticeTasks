# Create sha1 of possible combinations from AAAA to ZZZZ
# sha1 has been cryptographically broken and there are many replacements of it. 

def getCombinations(array, index):
    if index > -1: 
        if index == len(array)-1:
            while array[index] != 3:
                array[index] += 1
                print(array)
            else:
                array[index] = 0
                getCombinations(array, index-1)
        else:
            array[index] += 1
            if array[index] > 3:
                array[index] = 0
                getCombinations(array, index-1)
            else:
                getCombinations(array, index+1)

    return

def main():
    data = [1,1,1]
    print(data)
    getCombinations(data, len(data)-1)
