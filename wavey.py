import sys
import numpy as np
import time





CHARS = "·:-=+*#%@&▓█▄▀▌■"
class bg:
    def __init__(self):
        # wave parameters
        self.time = 0
        self.wave_speed = 1.5

    def generate_wave(self, xx, yy):
        # some funk ass math ;ol
        # makes the grid, x and y are the 1d matrix of the coords and the xx and yy are like each pixel 
        
        # print(xx.size)
        # print(yy.size)
        
        wave = (
            (np.cos(np.sqrt(xx**2 + yy**2) + self.time))+
            (np.cos(self.time) * np.sqrt(xx**2 + yy**2))+
            np.sin((xx + yy) * 1.5 + self.time * 0.7)+
            np.sin((xx * yy) * -1.5 + self.time * -0.7)+
            np.sin((xx * yy) * 8 + self.time * -0.9) 
        )
        # print(xx)
        
        
        
        wave = (wave - wave.min()) / (wave.max() - wave.min())
        return [[CHARS[int(value * 10)] for value in row] for row in wave]
    
    def draw_game(self):
        frame = self.generate_wave()
            
        sys.stdout.write("\033[H")
        sys.stdout.write("\n".join(["".join(row) for row in frame]))
        sys.stdout.flush()
