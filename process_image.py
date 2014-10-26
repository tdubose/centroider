import numpy as np
import cv2

def process_image(_frame,current_centroid,centroid_1,centroid_2,centroid_1_active,centroid_2_active):
	
	frame = _frame
	w,h, _ = frame.shape
	
	color_1 = (0,0,255)
	color_2 = (255,0,0)
	color_curr = (0,255,0)
	fontsize = 2.0
	fontface = cv2.FONT_HERSHEY_PLAIN
	
	line_offset = 20
	currtextpos = (0,w-1)
	cen1textpos = (0,w-1-line_offset)
	cen2textpos = (0,w-1-2*line_offset)
	
	
	#print type(frame)
	#print type((0,round(current_centroid[1]))
	#print type(w-1,round(current_centroid[1]))
	#print type(color_curr)
	              
	text_curr = 'Current centroid position %0.1f, %0.1f' % (current_centroid[0],current_centroid[1])
	cv2.putText(frame,text_curr,currtextpos,fontface,fontsize,color_curr)
	cv2.line(frame,(int(current_centroid[0]),0),(int(current_centroid[0]),w-1),color_curr)
	cv2.line(frame,(0,int(current_centroid[1])),(h-1,int(current_centroid[1])),color_curr)
	# 	# cv2.line(frame,(,0),(,h-1),color_curr)
	# 	cv2.line(frame,(,color_curr)
	# 	

	
	# draw active set centroids (and text display)
	
	if centroid_1_active:
		text_1 = 'Centroid 1 position %0.1f, %0.1f' % (centroid_1[0],centroid_1[1])
		cv2.putText(frame,text_1,cen1textpos,fontface,fontsize,color_1)
		cv2.line(frame,(int(centroid_1[0]),0),(int(centroid_1[0]),w-1),color_1)
		cv2.line(frame,(0,int(centroid_1[1])),(h-1,int(centroid_1[1])),color_1)
		
	if centroid_2_active:
		text_2 = 'Centroid 2 position %0.1f, %0.1f' % (centroid_2[0],centroid_2[1])
		cv2.putText(frame,text_2,cen2textpos,fontface,fontsize,color_2)
		cv2.line(frame,(int(centroid_2[0]),0),(int(centroid_2[0]),w-1),color_2)
		cv2.line(frame,(0,int(centroid_2[1])),(h-1,int(centroid_2[1])),color_2)
		
	return frame