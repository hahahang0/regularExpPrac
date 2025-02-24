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




# 7) Write a Python program to find sequences of lowercase letters joined with a underscore.


# def patternFunction(t_string):
#     pattern = r'^[a-z]+_[a-z]+$'
#     if re.findall(pattern,t_string):
#         return "Pattern Found"
#     else:
#         return "Pattern not found"


# print(patternFunction('hang'))
# print(patternFunction('abb'))
# print(patternFunction('abb_Bba'))
# print(patternFunction('abb_bba'))
# print(patternFunction('Abb_bba'))




# 8) Write a Python program to find the sequences of one upper case letter followed by lower case letters.


# def testFunction(t_string):
#     pattern = r'^[a-z]+_[A-Z]$'
#     if re.findall(pattern,t_string):
#         return "pattern found !"
#     else:
#         return "pattern not found !"


# print(testFunction("Hang"))
# print(testFunction("Hang_Thim"))
# print(testFunction("Hang_thim"))
# print(testFunction("hang_THIM"))


# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.


# def test_function(t_string):
#     pattern = r'a.*?b$'
#     if re.search(pattern,t_string):
#         return 'match found'
#     else:
#         return 'match not found'


# print(test_function("aaaa"))
# print(test_function("bbb"))
# print(test_function("bba"))
# print(test_function("aalkjlka;j;b"))

# Write a Python program that matches a word at the beginning of a string.


# def test_function(sentence):
#     pattern = r'\w+'
#     if re.findall(pattern,sentence):
#         return ("pattern found !")
#         # return pattern
#     else:
#         return "pattern not found !"


# print(test_function('Hello world!'))
# print(test_function('   Hello world!'))



# Write a Python program that matches a word at the end of string, with optional punctuation


# def test_function(sentence):
#     pattern = "\w+\S?$"
#     if re.search(pattern,sentence):
#         return "Match Found !"
#     else : 
#         return "match not found !"


# print(test_function("This is hangthim limbu"))
# print(test_function("This is hangthim limbu."))
# print(test_function("%(!%(*!%)!(*))"))


#  Write a Python program that matches a word containing 'z'

# def test_function(sentence):
#     pattern = r'z'
#     if re.findall(pattern,sentence):
#         return 'match found!'
#     else:
#         return 'match not found!'


# print(test_function('hello world !'))
# print(test_function('z aga;lkjgaj;l z'))
# print(test_function('z aga;lkjgaj;l '))
# print(test_function('aga;lkjzgaj;l '))
# print(test_function('hang z thim'))



    
# Solution
# def text_match(text):
#         patterns = '\w*z.\w*'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')

# print(text_match("The quick brown fox jumps over the lazy dog."))
# print(text_match("Python Exercises."))




# 13) Write a Python program that matches a word containing 'z', not at the start or end of the word.

# def test_function(sentence):
#     pattern = '\Bz\B'
#     if re.findall(pattern,sentence):
#         return 'match found!'
#     else :
#         return 'match not found'

# print(test_function('hello world'))
# print(test_function('zthisThat'))
# print(test_function('thitthatz'))
# print(test_function('heloo azb there'))
# # print(test_function('heloo z there'))


# 14) Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.


# def test_function(sentence):
#     pattern = r'^[a-zA-Z0-9_\s]*$'
#     if re.findall(pattern,sentence):
#         return "Match Found !"
#     else : 
#         return "Match not found"


# print(test_function('Hang thim'))
# print(test_function('1905'))
# print(test_function('%)*@'))

#  Write a Python program where a string will start with a specific number.

# def test_function(number):
#     pattern = r'^[0-9]'
#     if re.search(pattern,number):
#         return 'match found !'
#     else:
#         return 'match not found !'

# print(test_function('hangthim limbu'))
# print(test_function('1hangthim limbu'))
# print(test_function('hangthim limbu2'))




# 16) Write a Python program to remove leading zeros from an IP address

# def remove_leading_zeros_from_ip_string(ip_add):
#     pattern  = r'\.0*'
#     ip_add = re.sub(pattern,'.',ip_add)
#     return ip_add


# print(remove_leading_zeros_from_ip_string('192.168.01.01'))




# 17) Write a Python program to check for a number at the end of a string.


# def number_end_of_string(number):
#     pattern = r'[0-9]$'
#     if re.findall(pattern,number):
#         return "valid"
#     else : 
#         return "not valid"

# print(number_end_of_string('hangthim'))
# print(number_end_of_string('hangthim1'))
# print(number_end_of_string('1'))
# print(number_end_of_string('1hangthim'))


# 8) Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.

# def test_function(sentence):
#     pattern = r'([0-9]{1,3})'
#     result =  re.finditer(pattern,sentence)
#     return result


# result = test_function("Exercises number 1, 12, 13, and 345 are important")
# for ans in result:
#     print(ans.group(0))



# Solution
# results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
# print("Number of length 1 to 3")
# # print("result",results)
# for n in results:
#      print(n.group(0))


# Write a Python program to search some literals strings in a string. Go to the editor Sample text : 'The quick brown fox jumps over the lazy dog.' Searched words : 'fox', 'dog', 'horse'


# def search_some_literal_strings(sentence,t_list):
#     for pattern in t_list:
#           print('Searching for "%s" in "%s" ->' % (pattern,sentence),)
#           if re.search(pattern,sentence):
#                 print('match found')
#           else :
#                 print('match not found !')
  


# t_list = ['fox','lazy','dog']


# print(search_some_literal_strings('The quick brown fox jumps over the lazy dog',t_list))




# 20) Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs

# Sample text : 'The quick brown fox jumps over the lazy dog.' Searched words : 'fox'


# def search_literal_string_in_string(sentence,t_string):
#     result = re.search(t_string,sentence)
#     return result


# result = (search_literal_string_in_string('The quick brown fox jumps over the lazy dog','fox'))
# print(result.start())
# print(result.end())
# print(result.re.pattern)
# print(result.string)




# 21) Write a Python program to find the substrings within a string.

# Sample text :

# 'Python exercises, PHP exercises, C# exercises'

# Pattern :

# 'exercises'

# Note: There are two instances of exercises in the input string.


# def findSubstringsWithin_a_string(substring,string):
#     for match in re.findall(string, substring):
#         print('Found "%s"' % match)




# substring = 'Python exercises, PHP exercises, C# exercises'
# string = 'exercises'


# findSubstringsWithin_a_string(substring,string)



# 22) Write a Python program to find the occurrence and position of the substrings within a string.


# def find_occurence_and_position(string,pattern):
#     for matches in re.finditer(pattern,string):
#         print("start",matches.start())
#         print("end",matches.end())


# substring = 'Python exercises, PHP exercises, C# exercises'
# pattern = 'exercises'

# find_occurence_and_position(substring,pattern)


#  Write a Python program to replace whitespaces with an underscore and vice versa.

# def replace_whiteSpaces_with_underscore_and_vice_versa(words):
#     words = re.sub(' ','_',words)
#     print(words)
#     words = re.sub('_',' ',words)
#     print(words)



# replace_whiteSpaces_with_underscore_and_vice_versa('hang thim')


# 24) Write a Python program to extract year, month and date from a an url

# def extract_date_from_url(url):
#     pattern = r'/\d{4}/\d{1,2}/\d{1,2}/'
#     dateTime = re.findall(pattern,url)
#     return dateTime


# print(extract_date_from_url("https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"))





# 25) Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# def date_conversion(date):
#     result = re.sub(r'(\d{4})/(\d{1,2})/(\d{1,2})','\\3/\\2/\\1',date)
#     return result




# date  = '2020/11/12'
# print('original date',date)
# new_date   = date_conversion(date)
# print("date After conversion",new_date)


# 26) Write a Python program to match if two words from a list of words starting with letter 'P'.

# def check_if_words_from_list_match(t_list):
#     if re.match('h',t_list):
#         return 'matched !'
#     else:
#         return 'not matched !'



# check_if_words_from_list_match(['hang','thim','hang'])


# Write a Python program to separate and print the numbers of a given string.

# text = "ten 10 twenty 20 thirty 30"
# result = re.split(r'\D+',text)
# print(result)




# 28) Write a Python program to find all words starting with 'a' or 'e' in a given string.

# text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
# #find all the words starting with 'a' or 'e'
# list = re.findall("[a|e]\w+", text)
# # Print result.
# print(list)



# 30) Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.

def abbreviate_road_as_rd(t_string):
    t_string = re.sub(r'Road','Rd.',t_string)
    return t_string


print(abbreviate_road_as_rd('21 Ramkrishna Road Road'))