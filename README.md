# python-ascii-wave

A python script built using numpy that displays a wave effect in your cmd w unicode characters

was mainly built so i could mess around with numpy math & matrixes 


the wave is build using the equation

    wave = (

            (np.cos(np.sqrt(xx^2 + yy^2) + self.time))+
            
            (np.cos(self.time) * np.sqrt(xx^2 + yy^2))+
            
            np.sin((xx + yy) * 1.5 + self.time * 0.7)+
            
            np.sin((xx * yy) * -1.5 + self.time * -0.7)+
            
            np.sin((xx * yy) * 8 + self.time * -0.9) 
            
    )


xx & yy are matrixes with 120x50 weights in floats from 0-7 that determine the character that gets printed ( from ·:-=+*#%@&▓█▄▀▌■ )

xx stores x axis data while y holds y axis data



```
example xx matrix:
[
      [0.         0.05882353 0.11764706 ...skip 114... 6.88235294 6.94117647 7.        ]
      [0.         0.05882353 0.11764706 ...skip 114... 6.88235294 6.94117647 7.        ]
      [0.         0.05882353 0.11764706 ...skip 114... 6.88235294 6.94117647 7.        ]
      ...skip 44...
      [0.         0.05882353 0.11764706 ...skip 114... 6.88235294 6.94117647 7.        ]
      [0.         0.05882353 0.11764706 ...skip 114... 6.88235294 6.94117647 7.        ]
      [0.         0.05882353 0.11764706 ...skip 114... 6.88235294 6.94117647 7.        ]
]
```




### To run:
First,

`python -m pip install -r /requirements.txt`

Once done, run

`python -m reflex run` 

in the command line



### Demo:


https://github.com/user-attachments/assets/258a6b22-9d05-4201-9d2a-1d66c4fdba05



##### This script was built for [Hack Club High Seas](https://highseas.hackclub.com/)
