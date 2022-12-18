# change-calculator

My first proper project.

### Installed packages
OpenCV and needs to be installed before running this program.
This can be done by doing typing the following in the command prompt:
```
pip install opencv-contrib-python
```

### How to use
Comment out "while True" in Line 38, unless you are playing with trackbars. (NOT RECOMMENDED for first run)
Download the image named "all_coins2" and copy the file path. 
Paste the file path where the old file path is. (Lines 40 and 41)
If you receive an error, check the direction of the slashes. They must be '\' not '/' which is default on many machines.
Run the file to see output.

#### Trackbars
Uncomment all of the commented code. (Including the "while True" you would have commented out on your first try).
Comment out the second call of the HoughCircles function in Line 59.
Change the WaitKey interval from 0 to 300 in Line 113.
Run the code. 
This will bring an additional "Trackbar" window with arrows that can be dragged to alter the output almost real-time.

PLEASE NOTE: You will have to stop the terminal to close the image.

### Credits
1. A lot of the information about using OpenCV came from [this](https://www.youtube.com/watch?v=oXlwWbU8l2o&t=144s) FreeCodeCamp video on YouTube and [this](https://github.com/jasmcaus/opencv-course) GitHub repository from jasmcaus.
2. I learnt how to resize images from [here](https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/)
3. The trackbar tutorial on [this](https://www.youtube.com/watch?v=esmpHCJz8xI&list=WL&index=6) YouTube video by Giovanni code was very useful.
4. The OpenCV [docs](https://docs.opencv.org/2.4/modules/imgproc/doc/feature_detection.html?highlight=houghcircles)
5. Giles McMullen-Klein's Python Programmer Bootcamp course on [365DataScience](https://learn.365datascience.com/)
