from product import TV_interface, SamsungTV, LGTV, Aircon_interface, SamsungAircon, LGAircon


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

class home(bridge_plus):
    
    def __init__(self, tv:TV_interface, aircon:Aircon_interface):
        super().__init__(tv)
        self.aircon = aircon
        
    def now(self):
        print(self.tv.__class__.__name__)
        print(self.aircon.__class__.__name__)


my_home = home(SamsungTV(), LGAircon())

my_home.now()
my_home.turn_on()
my_home.mute()

#SamsungTV, LGTV 객체 합성 및 기능 확장
#Aircon 객체에는 영향 X