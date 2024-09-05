

class Book:

    title:str

    auther:str

    price:int

    language:str

    def __init__(self,title,auther,price,language):
        
        self.title=title

        self.auther=auther

        self.language=language

        self.price=price

    def display_book(self):

        print(self.title,self.auther,self.price,self.language)

book1=Book("nova","shameer",10000,"english")

book2=Book("ottbook","aseed",30000,"malayalam")

book1.display_book()

