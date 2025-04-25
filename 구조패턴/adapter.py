from typing import override


class origin():
    
    def print_string(self):
        
        print("hello world")

class client_interface():
    
    def print_hello_world(self):
        
        pass
    
class Adapter(client_interface):
    
    def __init__(self, adaptee):
        
        self.adaptee = adaptee
    
    @override
    def print_hello_world(self):
        
        self.adaptee.print_string()


client = Adapter(origin())
client.print_hello_world()
#client_interface가 origin 직접 상속X, client_interface method 사용