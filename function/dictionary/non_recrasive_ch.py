

text="adasaderw"

word_count={}

for w in text:

    if w in word_count:

        word_count[w]+=1

    else:

        word_count[w]=1

for a,b in word_count.items():

    if b==1:

        print(a)


