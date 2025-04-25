import copy


class Prototype():
    
    def clone(self):
        
        return copy.deepcopy(self)
    
class History(Prototype):
    
    def __init__(self, public, detail):
        
        self.public = public
        self.detail = detail
        
    def show(self):
        
        print(f'직위 : {self.public} : {self.detail}')
        
class Client():
        
    def next(self, previous, Ndetail):
        
        next_ver = previous.clone()
        next_ver.detail = Ndetail
        
        return next_ver

    
origin = History('도독', '주공근(~210)')

client = Client()
sec = client.next(origin, '노자경(~217)')
third = client.next(sec, '여자명(~219)')
forth = client.next(third, '육백언(~245)')

origin.show()
sec.show()
third.show()
forth.show()