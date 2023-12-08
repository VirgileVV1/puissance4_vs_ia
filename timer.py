class Timer:

    def __init__(self, ticks):
        self.initial_time = ticks
        self.current_time = ticks
        self.elapsed_time = 0

    def __str__(self):
        time = self.elapsed_time // 1000
        minutes = (time % 3600) // 60
        seconds = time % 60
        return "{:02d}:{:02d}".format(minutes, seconds)
    
    def update(self, ticks):
        self.current_time = ticks
        self.elapsed_time = self.current_time - self.initial_time