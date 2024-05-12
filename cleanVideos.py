import cv2
import time
import os

def CleanVideos():

    #Folder where the original videos are
    videosFile = os.listdir('videos/')
    
    #Checks if the folder exists
    if not os.path.isdir("video_images/"): 

        #If it doesn't exist, it's created 
        os.makedirs("video_images/") 

    #For each video in the folder
    for i in videosFile:

        #Runs the video
        cam = cv2.VideoCapture("videos/" + i)

        previousFrame1 = None
        previousFrame2 = None

        #Defines the minimum wait time between each saved image (seconds)
        waitTime = 0.5

        #Last time an image has been saved
        lastSaveTime = time.time()

        while True:

            ret, frame = cam.read()
            
            if not ret:
                break
            
            cv2.imshow("Video", frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break

            #Compares the current frame with the last two (that where saved)
            if previousFrame1 is not None and previousFrame2 is not None:
                diff1 = cv2.absdiff(frame, previousFrame1)
                diff2 = cv2.absdiff(frame, previousFrame2)
                diffSum1 = cv2.sumElems(diff1)[0] / (frame.shape[0] * frame.shape[1])
                diffSum2 = cv2.sumElems(diff2)[0] / (frame.shape[0] * frame.shape[1])
                
                #Defines the threshold to decide if two frames are similar enough
                threshold = 10  #It can be adjusted if necessary

                #Compares the thresholds
                if diffSum1 < threshold and diffSum2 < threshold:
                    #If they are similar enough, it saves the middle frame
                    if time.time() - lastSaveTime >= waitTime:
                        cv2.imwrite("video_images/frame_{}.png".format(cam.get(cv2.CAP_PROP_POS_FRAMES)), previousFrame1)
                        lastSaveTime = time.time()

            #Updates the previous frames with the actual ones
            previousFrame1 = previousFrame2
            previousFrame2 = frame.copy()
            
        
        cam.release()
        cv2.destroyAllWindows()
        
    
    return None
    
