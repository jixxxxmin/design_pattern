from abc import ABC, abstractmethod
from product import WindowButton, LinuxButton, Window_Checkbox, Linux_Checkbox


class Abstract_factory(ABC):
    
    @abstractmethod
    def button_click(self):
        
        pass
    
    @abstractmethod
    def checkbox_click(self):
        
        pass
    
class Window_factory(Abstract_factory):
    
    def button_click(self):
        
        return WindowButton()
    
    def checkbox_click(self):
        
        return Window_Checkbox()
    
class Linux_factory(Abstract_factory):
    
    def button_click(self):
        
        return LinuxButton()
    
    def checkbox_click(self):
        
        return Linux_Checkbox()
    
def client(test):
    
    btn = test.button_click()
    chk = test.checkbox_click()
    
    btn.click()
    chk.click()
    

client(Window_factory())