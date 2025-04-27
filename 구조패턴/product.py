from abc import abstractmethod


class Aircon_interface:
    
    @abstractmethod
    def on(self):
        pass
    @abstractmethod
    def off(self):
        pass

class SamsungAircon(Aircon_interface):
    
    def on(self):
        print("Samsung 에어컨 on") 
    def off(self):
        print("Samsung 에어컨 off")

class LGAircon(Aircon_interface):
    
    def on(self):
        print("LG 에어컨 on")
    def off(self):
        print("LG 에어컨 off")

class TV_interface:
    
    @abstractmethod
    def on(self):
        pass
    @abstractmethod
    
    def off(self):
        pass

class SamsungTV(TV_interface):
    
    def on(self):
        print("Samsung TV 켜짐")
    def off(self):
        print("Samsung TV 꺼짐")

class LGTV(TV_interface):
    
    def on(self):
        print("LG TV 켜짐")
    def off(self):
        print("LG TV 꺼짐")
    