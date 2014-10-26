from lib.device import Camera
from lib.interface import imshow, waitKey,destroyWindow, moveWindow
import numpy as np
import datetime
from centroid import centroid
from process_image import process_image

class getPulseApp(object):
    """
    Python application that finds a face in a webcam stream, then isolates the
    forehead.
    
    Then the average green-light intensity in the forehead region is gathered
    over time, and the detected person's pulse is estimated.
    """
    def __init__(self):
        #Imaging device - must be a connected camera (not an ip camera or mjpeg
        #stream)
        self.camera = Camera(camera=0) #first camera by default
        self.w,self.h = 0,0
        self.pressed = 0
        
        self.current_centroid = [0.0,0.0]
        
        self.centroid_1 = [0.0,0.0]
        self.centroid_2 = [0.0,0.0]
        
        self.centroid_1_active = False
        self.centroid_2_active = False
        
        #Maps keystrokes to specified methods
        #(A GUI window must have focus for these to work)
        self.key_controls = {"1" : self.set_centroid_1,
                             "2" : self.set_centroid_2}
    
    def set_centroid_1(self):
        """
        Sets centroid 1 to the current centroid position.
        If centroid 1 is not currently active, makes it active.
        """
        if not self.centroid_1_active:
            self.centroid_1_active = True
        
        self.centroid_1 = self.current_centroid
    
    def set_centroid_2(self):
        """
        Sets centroid 2 to the current centroid position.
        If centroid 2 is not currently active, makes it active.
        """
        if not self.centroid_2_active:
            self.centroid_2_active = True
        
        self.centroid_2 = self.current_centroid
    
    def key_handler(self):
        """
        Handle keystrokes, as set at the bottom of __init__()
        
        A plotting or camera frame window must have focus for keypresses to be
        detected.
        """
        
        self.pressed = waitKey(1) & 255 #wait for keypress for 10 ms
        if self.pressed == 27: #exit program on 'esc'
            print "exiting..."
            self.camera.cam.release()
            exit()
        
        for key in self.key_controls.keys():
            if chr(self.pressed) == key:
                self.key_controls[key]()
    
    def main_loop(self):
        """
        Single iteration of the application's main loop.
        """
        # Get current image frame from the camera
        frame = self.camera.get_frame()
        self.h,self.w,_c= frame.shape
        
        self.current_centroid = centroid(np.sum(frame,2)/3)
        
        #display unaltered frame
        #imshow("Original",frame)
        
        #collect the output frame for display
        output_frame = process_image(frame,self.current_centroid,self.centroid_1,self.centroid_2,self.centroid_1_active,self.centroid_2_active)
        
        #show the processed/annotated output frame
        imshow("Processed",output_frame)
        
        #handle any key presses
        self.key_handler()

if __name__ == "__main__":
    App = getPulseApp()
    while True:
        App.main_loop()
