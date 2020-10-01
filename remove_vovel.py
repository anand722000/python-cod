#this code will remove all vowels from string
def remove_vowel(n):
    string=""
    for i in tuple(n):  #converting string in tuple
        if i not in ['a','e','i','o','u','A','E','I','O','U']:
            string=string+i
    print(string)

n=input()
remove_vowel(n)



