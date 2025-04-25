
class Singleton():
    
    check_instance = None
    num = 0
    
    def __new__(cls):
        
        if cls.check_instance == None:
            
            print('Create new instance')
            
            cls.check_instance = super().__new__(cls)
            
        return cls.check_instance
    
    def __init__(self):
        
        self.num += 1
    
    def __str__(self):
        
        return f"{self.num}"


s1 = Singleton()
s2 = Singleton()

print(s1 == s2)
print(s1.num, s2.num)