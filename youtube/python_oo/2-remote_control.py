class RemoteControl():
    
    def __init__(self, tv = 'Samsumg', room = 'Bedroom'):
        
        self.tv      = tv
        self.room    = room
        self.channel = 12
        
        
    def channel_foward(self):
        self.channel += 1
        print(f"Channel: {self.channel}")
        
    def channel_back(self):
        self.channel -= 1
        print(f"Channel: {self.channel}")
        
    def choose_channel(self, chosen_channel = 12):
        self.channel = chosen_channel
        print(f"Channel: {self.channel}")
        
control_bathroom = RemoteControl('LG', 'Bathroom')
control_bathroom.channel_foward()
control_bathroom.channel_foward()
control_bathroom.channel_foward()
control_bathroom.channel_back()
print(control_bathroom.tv, control_bathroom.room, control_bathroom.channel)

print('-' * 20)

control_bedroom = RemoteControl('Samsung', 'Bedroom')
print(control_bedroom.tv, control_bedroom.room)
chosen_channel = int(input("Channel to choose: "))
control_bedroom.choose_channel(chosen_channel)
