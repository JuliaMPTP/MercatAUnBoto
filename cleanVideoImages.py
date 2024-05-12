import matplotlib.pyplot as plt
import cv2
import os


def cleanVideoImages():

    #Folder with the images extracted from the videos
    imagesFile = os.listdir('video_images/')

    #Checks if the folder exists
    if not os.path.isdir("clean_images/"): 

        #If it doesn't exist, it's created 
        os.makedirs("clean_images/") 

    #For each image in the folder
    for i in imagesFile: 
        
        #Reads the image and turns it to gray scale
        image = cv2.imread("video_images/" + i)
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #It uses canny on the image to detect the contours
        cannyImage = cv2.Canny(grayImage, 50,50)
        cannyImage = cv2.dilate(cannyImage, None, iterations=1)
        cannyImage = cv2.erode(cannyImage, None, iterations=1)
        contours, _ = cv2.findContours(cannyImage, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        #Creates a list with all the areas
        areasList = []
        for c in contours:
            area = cv2.contourArea(c)
            areasList.append(area)

        #Searches for the biggest contour
        biggestArea = contours[areasList.index(max(areasList))]

        #It keeps the area of interest in the image (gray scale)
        x,y,w,h = cv2.boundingRect(biggestArea)
        finalImage = grayImage[y:y+h, x:x+w]
        finalImage = cv2.cvtColor(finalImage, cv2.COLOR_GRAY2RGB)

        #plt.imshow(finalImage)
        #plt.show()
        #cv2.waitKey(0)
        
        #Saves the image in a different folder
        cv2.imwrite("clean_images/" + i, finalImage)
        
        #Removes the image from the folder so next time it doesn't repeat
        os.remove("video_images/" + i)
        
    return None



