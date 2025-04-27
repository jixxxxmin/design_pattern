
class people1():
    
    def __init__(self):
        self.name = "장소"
        
    def show(self):
        print(f'- {self.name}')
    
class people2():
    
    def __init__(self):
        
        self.name = "장굉"
        
    def show(self):
        print(f'- {self.name}')

class people3():
    
    def __init__(self):
        self.name = "주유"
    
    def show(self):
        print(f'- {self.name}')

class people4():
    
    def __init__(self):
        self.name = "노숙"
    
    def show(self):
        print(f'- {self.name}')

class red_cliff():
    
    def __init__(self, name):
        self.name = name
        self.people = []
    
    #component가 없어서, 하나만 method 이름 바꿨는데 벌써 길어짐
    def show_a(self):
        print(f'{self.name}')
        
        for i in self.people:
            if isinstance(i, people1) or isinstance(i, people2) or isinstance(i, people3) or isinstance(i, people4):
                i.show()
            elif isinstance(i, red_cliff):
                i.show_a()
            else:
                print("error")
        
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
history.show_a()