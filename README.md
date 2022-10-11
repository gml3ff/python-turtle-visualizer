# python-turtle-visualizer


Exceedingly basic visualizer that uses two very basic components (the audio analysis part of this is not yet completed). 

- **multi_cube.py** - Creates randomly sized cubes that recede to a central point on the screen
- **librosa-test.py** - Computes spectral centroid at multiple frequencies on the default audio input device and outputs the result. Future intent is to combine this using some multi-threaded approach in conjunction with `multi_cube.py` in order to do real-time audio analysis. 
