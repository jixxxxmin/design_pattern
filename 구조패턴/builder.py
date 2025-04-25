
class TV_interface:
    
    def on(self):
        pass
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
        
class bridge:
    
    def __init__(self, tv:TV_interface):
        self.tv = tv

    def turn_on(self):
        self.tv.on()

    def turn_off(self):
        self.tv.off()
        
class bridge_plus(bridge):
    
    def mute(self):
        print("음소거")
    

remote1 = bridge_plus(SamsungTV())
remote1.turn_on()
remote1.mute()