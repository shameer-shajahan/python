

f=open("/Users/shameershajahan/Desktop/PythonJune/fileoperator/land_slide.txt","r")

# land_slide=[]

# for line in f:

#     land=line.rstrip("\n")

#     land=land.split(" ")
    
#     for w in land:

#         land_slide.append(w)

# # print(land_slide)

# wc={w : land_slide.count(w) for w in land_slide}

# # print(wc)

# def get_value(key):

#     return wc.get(key)

# srt=sorted(wc,key=get_value,reverse=True)

# print(srt)


data=[]

for line in f:
    # print(line)

    lst=line.rstrip("\n").split(" ") 

    dic={"state":lst[0],"year":[1],"death_count":int(lst[2])}

    data.append(dic)

print(data)

state_summary={}

for dic in data:

    state=dic.get("state")

    death_count=dic.get("death_count")

    if state in state_summary:

        state_summary[state]+=death_count

    else:

        state_summary[state]=death_count

# print(state_summary)



