from abc import ABC, abstractmethod


class Button():
    
    @abstractmethod 
    def click(self):
        
        pass
    
class WindowButton(Button):
    
    def click(self):
        
        print("Window Button")
        
class LinuxButton(Button):
    
    def click(self):
        
        print("Linux Button")
        
class Checkbox():
    
    def hello(self):
        
        print("hello")
        
    @abstractmethod    
    def click(self):
        
        pass
    
class Window_Checkbox(Checkbox):
    
    def click(self):
        
        print("Window Checkbox")
        
class Linux_Checkbox(Button):
    
    def click(self):
        
        print("Linux Checkbox")
