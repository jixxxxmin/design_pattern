from abc import ABC, abstractmethod
from product import WindowButton, LinuxButton, Window_Checkbox, Linux_Checkbox


class Factory_method(ABC):
    
    @abstractmethod
    def button_click(self):
        
        pass
        
    @abstractmethod
    def checkbox_click(self):
    
        pass
    
    def render(self):
        
        btn = self.button_click()
        chk = self.checkbox_click()
        
        btn.click()
        chk.click()
        
class Window_method(Factory_method):
    
    def button_click(self):
        
        return WindowButton()
        
    def checkbox_click(self):
        
        return Window_Checkbox()

class Linux_method(Factory_method):
    
    def button_click(self):
        
        return LinuxButton()
        
    def checkbox_click(self):
        
        return Linux_Checkbox()

def client(test):
    
    test.render()
    

client(Window_method())