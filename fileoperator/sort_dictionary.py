placement={"django":35,"bigdata":45,"java":23,"pbi":32,"testing":30}

def get_value(key):

    return placement.get(key)


srt=sorted(placement,key=get_value,reverse=True)
print(srt)



