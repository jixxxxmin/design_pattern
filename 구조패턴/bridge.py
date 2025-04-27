from product import TV_interface, SamsungTV, LGTV


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