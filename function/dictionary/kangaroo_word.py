

word="CHIKEN"

target="HENC"

is_kangaroo=True

word_count={}

target_count={}

for w in word:

    if w in word_count:

        word_count[w]+=1

    else:

        word_count[w]=1

if w in target and word_count.get(w)>0 :

    word_count[w]-=1

else:
    
    is_kangaroo=False

print(is_kangaroo)