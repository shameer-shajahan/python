word="demo count"

vowel="aeiou"
count=0
for ch in word:
    if vowel.count(ch)!=0:
        count+=1
print(count)
