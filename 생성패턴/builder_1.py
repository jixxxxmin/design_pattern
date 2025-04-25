
class Burger:
    
    def __init__(self):
        
        self.parts = []
        
    def add(self, part):
        
        self.parts.append(part)
        
    def show(self):
        
        print("Burger : ", ", ".join(self.parts))
        
class BurgerBuilder:
    
    def __init__(self):
        
        self.burger = Burger()
        
    def add_bun(self):
        
        self.burger.add("Bun")
    
    def add_patty(self):
        
        self.burger.add("Patty")
        
    def add_sauce(self):
        
        self.burger.add("sauce")

    def add_lettuce(self):
        
        self.burger.add("lettuce")
        
    def get_burger(self):
        
        return self.burger
    
class BurgerDirector:
    
    def __init__(self, builder):
        
        self.builder = builder
    
    def make_burger(self):
        
        self.builder.add_bun()
        self.builder.add_sauce()
        self.builder.add_patty()
        self.builder.add_lettuce()
        self.builder.add_bun()
        
def client():
    
    builder = BurgerBuilder()
    director = BurgerDirector(builder)
    
    director.make_burger()
    
    burger = builder.get_burger()
    burger.show()
    

client()