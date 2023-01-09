## Tasks Details

### TASK 1

1. Here are some encoded strings that we need to decode either using online decoder or with the help of any programming language, personally I am trying to solve these strings using python.

	1. ***Ceaser Cypher*** : Dlsjvtl av ulazxbhyl
		
		Explanation: We don't have any `shift key` available to decode this string, in one of the online decoders I've seen that they are using 7 as the default shift key value, but here's a twist, we will find out what's the correct `shift key` and what's the correct decoded version of this string. 

		**Requirements :**  
		File: words_dictionary.json  
		Download it from [url](https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json)
		
		**Source File :** decodeCaeserCipher.py  
        	**Method :** SolveCiphers().caeserCipher()  <br><br>
		
	2. ***Morse Code*** : .-- . .-.. -.-. --- -- . / - --- / -. ... -.-. .

		Explanation: We have this string encoded in a morse code format, morse code is basically a technique where we represents numbers, letters, punctuations in the form of dot & dashes. We can also represent morse code in binary, but for this task, we will use the dot-dash style for the encoded output.  
		  
		**Requirements :**  
		File: morse-code.json
		This file is necessary because it contains a dictionary of letters, number, punctuations and their associated morse code representation.  
		  
		**Source File :** morseCodeEncodeDecode.py  
		**Method :** main() <br><br>
