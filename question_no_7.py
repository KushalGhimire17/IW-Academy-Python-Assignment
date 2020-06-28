word_list = []
user_response = ''
while user_response.casefold() != 'n':
    user_input = input("Enter a list of words: ")
    word_list.append(user_input)
    user_response = input("Do you want to input more words [y/n] ?")
print(word_list)

def longest_word():
    long_word_count = 0
    for word in word_list:
        if len(word) > long_word_count:
            long_word_count = len(word)
            long_word = word
    print("The longest word is {0} whose count is {1}...".format(long_word,long_word_count))

if __name__ == "__main__":
    longest_word()