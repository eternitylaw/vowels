vowels="Milliways"
vowels=['a','e','i','o','u']
found=[]
word=input("Provide a word to search for vowels:")
for char in word:
        if char in vowels:
            if char not in found:
                found.append(char)
for vowel in found:
    print(vowel)
                    
