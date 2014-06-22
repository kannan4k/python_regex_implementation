"""Implementation of the Python Programming Contest 1"""
from __builtin__ import range

def split_string(text):
    """ This function will split the string into list based on the '*' as delimiter
        For Ex: input = "Hello*Python"
                Output = ['Hello', 'Python']
                and Yes it will remove the \ in the string also """
    previous = 0
    word_list = []
    for index in range(len(text)):
        if text[index] == '*' and text[index-1] != '\\':
            if text[previous:index]:
                word = ''
                for x in text[previous:index]: #strip of escape sequence char
                    if x != '\\':
                        word += x
                word_list.append(word) 
                previous = index+1
    else:
        word = ''
        for x in text[previous:]:
            if x != '\\':
                word += x
        word_list.append(word)
    return word_list

def substring(pattern, text):
    """ main substring function which will check for the sequential lists """
    pos = 0
    is_valid = True
    msg = "%s is a substring of %s" % (pattern, text)
    words = split_string(pattern)
    for word in words:
        n = find_replica(text, word, pos)
        if n < 0:
            msg = "%s is not a substring of %s" % (pattern, text)
            is_valid  = False 
            return is_valid, msg
        pos = n + len(word)
    return is_valid, msg

def find_replica(text, word, pos):
    """ implementation of the string find replica - simple string searching function """
    is_valid = -1
    length_1 = len(text)
    length_2 = len(word)
    while (pos <= length_1-length_2):
        for index_2 in range(length_2):
            if text[pos+index_2] != word[index_2]:
                is_valid = -1
                break
            is_valid = True
        else:
            is_valid = pos
            break
        pos += 1
    return is_valid


if __name__ == "__main__":
    ### Inputs ### 
    string_2 = raw_input("Enter the String1 or Just Hit Enter Key to see the results for given strings")
    if not string_2:
        string_1 = "H\*l*23"
        _, result = substring('Hello1', "Hello")
        print result
        _, result = substring('H\*l*23', "H*lllo123")
        print result
        _, result = substring('Hel*23', "123Hello")
        print result
        _, result = substring('Hello*How', "Hello*How are you?")
        print result
    string_1 = raw_input("Enter a Pattern (string2) or Just Hit Enter Key to see the results for given strings")
    _, result = substring(string_1, string_2)
    print result

