import collections

user_input = input("Enter a sentence...")
words = user_input.split()
word_counts = collections.Counter(words)
word_list = []

for word, count in word_counts.items():
    if word not in word_list:
        word_list.append(word)
else:
    print(word_list)


#  NEXT METHOD 
# from itertools import groupby
# user_input = input("Enter a sentence...")
# words = user_input.split()
# word_list = []
# for word, duplicates in groupby(sorted(words)):
#     count = len(list(duplicates))
#     print('"{word}" is repeated {count} time{s}'.format(
#             word=word, count=count,  s='s'*(count > 1)))
#     if word not in word_list:
#         word_list.append(word)
# print(word_list)