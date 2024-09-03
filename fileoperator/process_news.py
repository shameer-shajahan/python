f=open("/Users/shameershajahan/Desktop/PythonJune/fileoperator/news.txt","r")

# word_list=[]
# for line in f:
#     word=line.rstrip("\n")

#     word=word.split(" ")
    
#     for w in word:

#         word_list.append(w)

# print(word_list)

word_list=[w for line in f for w in line.rstrip("\n").split(" ")if w!=""]

# print(word_list)

wc={w : word_list.count(w) for w in word_list}

# print(wc)

def get_value(key):

    return wc.get(key)

srt=sorted(wc,key=get_value,reverse=True)
print(srt)