import shutil
import numpy as np
import time
import sys
import wavey
from digits import DIGITS

class Clock:
    def __init__(self):
        try:
            self.width, self.height = shutil.get_terminal_size((80, 24))
        except:
            self.width, self.height = 80, 24
        self.x = np.linspace(0, 7, self.width) 
        self.y = np.linspace(0, 7, self.height)
        self.xx, self.yy = np.meshgrid(self.x, self.y)
        self.bg = wavey.bg()
    
    def draw_big_clock(self, frame):
        time_str = time.strftime("%I:%M %p")
        rows = len(frame)
        cols = len(frame[0]) if rows > 0 else 0
        
        clock_width = len(time_str) * 8 # every digit is 7 wide + 1 space
        clock_height = 7
        start_row = int((rows - clock_height) / 2)
        start_col = int((cols - clock_width) / 2)
        
        if start_row < 0 or start_col < 0:
            return frame  # toooo smallll
        
        for i, char in enumerate(time_str):
            # print(char)
            if char not in DIGITS:
                continue
            digit = DIGITS[char]
            for y, line in enumerate(digit):
                for x, block in enumerate(line):
                    if block == '█':
                        frame_row = start_row + y
                        frame_col = start_col + x + (i * 8)
                        if 0 <= frame_row < rows and 0 <= frame_col < cols:
                            frame[frame_row] = (
                                frame[frame_row][:frame_col] + # everything before
                                "█" +
                                frame[frame_row][frame_col+1:] # everything after
                            )
        return frame
    def draw(self):
        wave = self.bg.generate_wave(self.xx, self.yy)
        frame = ["".join(row) for row in wave]
        frame = self.draw_big_clock(frame)
        
        sys.stdout.write("\033[H")  # Move cursor home
        sys.stdout.write("\n".join(frame))
        sys.stdout.flush()
    def run (self):
        while True:
            current_size = shutil.get_terminal_size().columns, shutil.get_terminal_size().lines
            if current_size != (self.width, self.height):
                try:
                    self.width, self.height = shutil.get_terminal_size((80, 24))
                except:
                    self.width, self.height = 80, 24
                x = np.linspace(0, 7, self.width) 
                y = np.linspace(0, 7, self.height)
                self.xx, self.yy = np.meshgrid(x, y)
            
            
            
            self.bg.time += 0.1 * 1
            self.draw()
            time.sleep(0.05)

if __name__ == "__main__":
    c = Clock()
    c.run()
    
    