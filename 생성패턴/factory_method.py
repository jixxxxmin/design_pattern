from abc import ABC, abstractmethod
from product import WindowButton, LinuxButton


class Factory_method(ABC):
    
    @abstractmethod
    def button_click(self):
        
        pass
    
    def render(self):
        
        btn = self.button_click()
        btn.click()
        
class Window_method(Factory_method):
    
    def button_click(self):
        
        return WindowButton()
    
class Linux_method(Factory_method):
    
    def button_click(self):
        
        return LinuxButton()
    
def client(test):
    
    test.render()
    

client(Linux_method())