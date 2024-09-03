

# word=["hello","hello","hi","hai","hai","hai"]


# # // logic = 1


# word_count={}

# for w in word:

#     if w in word_count:

#         word_count[w]+=1

#     else:

#         word_count[w]=1


# print(word_count)


text="hello hai hi hello hai "

word=text.split( )

dict_word={}

for w in word:

    if w in dict_word:

        dict_word[w]+=1

    else:

        dict_word[w]=1

print(dict_word)

