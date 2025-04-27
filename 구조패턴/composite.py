from abc import ABC, abstractmethod


class menu():
    
    @abstractmethod
    def show(self):
        pass
    
class people1(menu):
    
    def __init__(self):
        self.name = "장소"
        
    def show(self):
        print(f'- {self.name}')
    
class people2(menu):
    
    def __init__(self):
        
        self.name = "장굉"
        
    def show(self):
        print(f'- {self.name}')

class people3(menu):
    
    def __init__(self):
        self.name = "주유"
    
    def show(self):
        print(f'- {self.name}')

class people4(menu):
    
    def __init__(self):
        self.name = "노숙"
    
    def show(self):
        print(f'- {self.name}')

class red_cliff(menu):
    
    def __init__(self, name):
        self.name = name
        self.people = []
    
    def show(self):
        print(f'{self.name}')
        for i in self.people:
            i.show()
        
    def add(self, name):
        self.people.append(name)
        

history1 = red_cliff("[주화파]")
history1.add(people1())
history1.add(people2())

history2 = red_cliff("[주전파]")
history2.add(people3())
history2.add(people4())

history = red_cliff("🔥적벽🔥")
history.add(history1)
history.add(history2)
history.show()