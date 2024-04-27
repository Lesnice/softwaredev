def alternate_char(text):
    """converts alternate characters in a string to upper and lower cases.
    
    arg: text which is an input.
    returns a new string with alternate characters
    """
    result = " "
    for i, word in enumerate(text):
        if i % 2 ==0:
            result += word.upper()
        else:
            result += word.lower()
    return result
text = input("enter text:")
print(alternate_char(text))        


def alternate_word(word):
    
    """converts alternate words in a string to uppercase.
    
    arg: input string"""
    
    words =word.split()
    
    updated_words = []
    
    for index, word in enumerate(words):
        
        if index % 2 ==0:
            updated_words.append(word.lower())
        else:
            updated_words.append(word.upper())
            
    updated_words = " ".join(updated_words)
    
    return updated_words
word= input('Enter a string:')
print(alternate_word(word))