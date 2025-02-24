import re 


# 1) Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

# def specificChar(t_string):
#     compiled_exp = re.compile(r'\w+')
#     string = compiled_exp.search(t_string)
#     return  bool(string)


# print(specificChar('hang'))
# print(specificChar('$#^!^!^&*(#)'))



# Solution
# def is_allowed_specific_char(string):
#     charRe = re.compile(r'[^a-zA-Z0-9.]')
#     string = charRe.search(string)
#     return not bool(string)

# print(is_allowed_specific_char("ABCDEFabcdef123450")) 
# print(is_allowed_specific_char("*&%@#!}{"))


#Write a Python program that matches a string that has an a followed by zero or more b's

# def followedByA_and_zero_more_b_s(t_string):
#     if t_string : 
#         if re.search(r'ab*?',t_string):
#             return "pattern matches"
#         else:
#             return 'pattern does not match'
        



# print(followedByA_and_zero_more_b_s('ac'))

# Solution
# def text_match(text):
#         patterns = r'ab*'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')

# print(text_match("ac"))
# print(text_match('bab'))
# print(text_match('amg'))
# print(text_match("abc"))
# print(text_match("abbc"))



# Define the pattern to match 'a' followed by zero or more 'b's
# pattern = r'ab*'

# Function to check if the string matches the pattern
# def match_string(string):
#     if re.fullmatch(pattern, string):
#         return True
#     else:
#         return False

# # Test examples
# test_strings = ['a', 'ab', 'abb', 'abbb', 'b', 'ba', 'abc']
# for string in test_strings:
#     result = match_string(string)
#     print(f"'{string}': {result}")


# 3) Write a Python program that matches a string that has an a followed by one or more b's

# def followedByOneOrMoreBees(t_string):
#     pattern = r'b+'
#     if re.search(pattern,t_string):
#         return "match found"
#     else :
#         return 'match not found'
    

# print(followedByOneOrMoreBees('hang'))
# print(followedByOneOrMoreBees('bee'))



# 4) Write a Python program that matches a string that has an a followed by zero or one 'b'

# def thisFunction(t_string):
#     pattern = r'ab?'
#     if re.search(pattern,t_string):
#         return "match found"
#     else :
#         return 'match not found'
    

# print(thisFunction('hag'))
# print(thisFunction('bb'))
# print(thisFunction('aba'))
# print(thisFunction('abbbbb'))


# Solution
# def text_match(text):
#         patterns = 'ab?'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')

# print(text_match("ab"))
# print(text_match("abc"))
# print(text_match("abbc"))
# print(text_match("aabbc"))


# 5) Write a Python program that matches a string that has an a followed by three 'b'


# def text_match(t_string):
#     pattern = r'ab{3}?'
#     if re.search(pattern,t_string):
#         return "Match Found !"
#     else :
#         return "Match not Found !"
    
# print(text_match('hang'))
# print(text_match('aaa'))
# print(text_match('abbb'))




# 6) Write a Python program that matches a string that has an a followed by two to three 'b'.

# def text_match(t_string):
#     pattern = r'ab{2,3}?'
#     if re.search(pattern,t_string):
#         return 'Match Found'
#     else :
#         return 'Match not found'
    

# print(text_match('hang'))
# print(text_match('ab'))
# print(text_match('abb'))
# print(text_match('abbbb'))


# Write a Python program to find the sequences of one upper case letter followed by lower case letters


def upper_lower(t_str):
    pattern = r'a-zA-Z'
    
