from abc import ABC, abstractmethod
from product import WindowButton, LinuxButton


class Abstract_factory(ABC):
    
    @abstractmethod
    def button_click(self):
        
        pass
    
class Window_factory(Abstract_factory):
    
    def button_click(self):
        
        return WindowButton()

class Linux_factory(Abstract_factory):
    
    def button_click(self):
        
        return LinuxButton()
    
def client(test):
    
    btn = test.button_click()
    
    btn.click()
    

client(Window_factory())