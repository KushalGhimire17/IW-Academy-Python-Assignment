"""
Check anagrams words from paragraph
"""

sample_paragraph = input("Enter a paragraph: ")
user_word_input = input("Enter a word: ")
words_from_paragraph = sample_paragraph.split(' ')

for char in words_from_paragraph:
    if(sorted(char) == sorted(user_word_input)):
        print("WORD: '{}' and PARAGRAPH_WORD: '{}' are anagrams.".format(user_word_input, char))