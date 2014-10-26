import numpy as np

def centroid(image):
	w, h = image.shape # gets width of image
	cX, cY = np.meshgrid(range(0,h),range(0,w)) #gets weighted coordinate matrices
	centroid_x = np.mean(cX*image)/np.mean(image)
	centroid_y = np.mean(cY*image)/np.mean(image)
	return [centroid_x, centroid_y]