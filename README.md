## Tasks Details

### TASK 1

1. Here are some encoded strings that we need to decode either using online decoder or with the help of any programming language, personally I am trying to solve these strings using python.

	1. ***Ceaser Cypher*** : Dlsjvtl av ulazxbhyl
		
		Explanation: I don't have any `shift key` available to decode this string, in one of the online decoders I've seen that they are using 7 as the default shift key value, but here's a twist, I will find out what's the correct `shift key` and what's the correct decoded version of this string. 

		**Requirements :**  
		File: words_dictionary.json  
		Download it from [url](https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json)
		
		**Source File :** decodeCaeserCipher.py  
        	**Method :** SolveCiphers().caeserCipher()  <br><br>
		
	2. ***Morse Code*** : .-- . .-.. -.-. --- -- . / - --- / -. ... -.-. .

		Explanation: I have this string encoded in a morse code format, morse code is basically a technique where we represents numbers, letters, punctuations in the form of dot & dashes. We can also represent morse code in binary, but for this task, I will be using the dot-dash style for the encoded output.  
		  
		**Requirements :**  
		File: morse-code.json  
		This file is necessary because it contains a dictionary of letters, number, punctuations and their associated morse code representation.  
		  
		**Source File :** morseCodeEncodeDecode.py  
		**Method :** main() <br><br>
		
	3. ***Binary*** : 01110111 01101000 01100001 01110100 00100000 01101001 01110011 00100000 01111001 01101111 01110101 01110010 00100000 01101110 01100001 01101101 01100101 00111111  
		  
		Explanation: Decode this binary string into a human readable text, here the thing is, in python let's say which is what I'm using, the binary format of a letter is represented as '0b111111', '0b' as a prefix. Although both are acceptable.  
		  
		**Source File :** binaryEncodeDecode.py  
		**Method :** main() <br><br>
		  
	4. ***Url Encoding*** : Do%21you%28know%29%23URL%2aencoding%5cis%2ffun%3f  
	  
	  	Explanation: The above string is encoded with the url encoding, means some of the characters present in the string has been replaced with their ascii value, which then later converted into the hex. For example: the punctuation "!" ascii value is 33, convert this value into hex, we will get "0x21". In a similar way, the string contains many more like this.  
		  
		**Souce File :** urlencoding.py  
		**Method :** main() <br><br>
		
	5. ***Unicode Encoding*** : %u0045%u006e%u0063%u006f%u0064%u0065%u0020%u0077%u0069%u0074%u0068%u0020%u0055%u006e%u0069%u0063%u006f%u0064%u0065%u0020%u0065%u006e%u0074%u0069%u0074%u0079  
	  
		Explanation: Decode the above text which is unicode encoded. Unicode is used to provide each characters in any language, either latin, american, british, indian, characters a unique code point. This is necessary because after all, in order to understand and get it accepted by the machine, it needs to be converted to a machine language, and in order to convert a character into a machine language, we should know how to represent it in an integer. For further readings about why the code points is necessary and representation of unicode characters, you can go through this [Documentation](https://docs.python.org/3/howto/unicode.html)  
		
		**Source File :** unicode.py <br><br>
		
	6. ***SHA-1*** : known as *Secure Hash Algorithm 1*, In this task, There will be possible combination of alphabets, from AAAA to ZZZZ, and it has been asked to find the SHA-1 of all the combinations and print the combination plus their SHA-1.  
	  
		**Possible Combinations :**   
		AAAA,  
		AAAB,   
		...  
		AAAZ,  
		AABA,  
		AABB,  
		AABZ,  
		...  
		ZZZZ  
		<br>
		**Output :**   
		AAAA,e2512172abf8cc9f67fdd49eb6cacf2df71bbad3  
		AAAB,a8aefbd08cdb3eb98efe00a915ff5f3670c3cb78  
		...  
		...  
		ZZZZ,9865d483bc5a94f2e30056fc256ed3066af54d04  
