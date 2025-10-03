class Television:

    def __init__(self,turn_on,turn_off):
        self.turn_on = turn_on
        self.turn_off = turn_off

    def watch(self):
        self.turn_on = 'program'
        self.turn_off = 'blank'

        return self.turn_on,self.turn_off
    
tv = Television('turn_on','turn_off')

print(tv.watch())