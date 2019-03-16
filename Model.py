class Model():
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_model = None
        self.buttons = []
        self.persist = {}
                
    def startup(self, persistent):
        self.persist = persistant
        
    def update(self, frame_time):
        pass
        
    def get_event(self, event):
        pass
    
    def draw(self, display):
        pass
    