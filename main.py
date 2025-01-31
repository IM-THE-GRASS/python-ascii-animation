import sys
import numpy as np
import time





CHARS = "·:-=+*#%@&▓█▄▀▌■"
class funycmdwave:
    def __init__(self):
        self.width, self.height = 120, 50
        
        # wave parameters
        self.time = 0
        self.wave_speed = 1.5

    def generate_wave(self):
        # some funk ass math ;ol
        # makes the grid, x and y are the 1d matrix of the coords and the xx and yy are like each pixel 
        x = np.linspace(0, 7, self.width) 
        y = np.linspace(0, 7, self.height)
        xx, yy = np.meshgrid(x, y)
        # print(xx.size)
        # print(yy.size)
        
        wave = (
            (np.cos(np.sqrt(xx**2 + yy**2) + self.time))+
            (np.cos(self.time) * np.sqrt(xx**2 + yy**2))+
            np.sin((xx + yy) * 1.5 + self.time * 0.7)+
            np.sin((xx * yy) * -1.5 + self.time * -0.7)+
            np.sin((xx * yy) * 8 + self.time * -0.9) 
        )
        
        
        
        wave = (wave - wave.min()) / (wave.max() - wave.min())
        return [[CHARS[int(value * 10)] for value in row] for row in wave]
    
    def draw_game(self):
        """Render game state with wave background"""
        frame = self.generate_wave()
            
        sys.stdout.write("\033[H")
        sys.stdout.write("\n".join(["".join(row) for row in frame]))
        sys.stdout.flush()
    
        

    def run(self):
        while True:
            self.time += 0.1 * self.wave_speed
            self.draw_game()
            time.sleep(0.05)

if __name__ == "__main__":
    game = funycmdwave()
    game.run()