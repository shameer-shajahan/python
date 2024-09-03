word="consonents demo"
vowels="aeiou"
count=0
for ch in word:
    if vowels.count(ch)==0:
        count+=1
print(count)