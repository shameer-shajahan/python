word1="pqrs"

word2="ABCDEFG"

smallest_word = word1 if len(word1) > len(word2) else word2

merge_str=""

for i in range(0,len(smallest_word)):

    merge_str=(merge_str + (word1[i]+word2[i]))

if len(word1) > len(word2):

    balance=word1[len(smallest_word):]

else:

    balance=word2[len(smallest_word):]

merge_str=merge_str+balance

print(merge_str)
