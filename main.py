import os
from cleanVideos import CleanVideos
from cleanVideoImages import cleanVideoImages
from RunAPI import pentoprint
from convertCSV import convertCSV

#Change the "API_Key" to yours
API_Key= "API_Key"

#Save the values returned by the API
vals=[]

def main():

    #Cleans the videos and extracts the images
    CleanVideos()
    
    #cleans the images and saves the results of the API
    cleanVideoImages()
    result = pentoprint(API_Key)

    #Folder with the already clean images
    cleanImagesFile = os.listdir('clean_images/')

    for i in cleanImagesFile:
        #Removes the image from the folder so next time it doesn't repeat
        os.remove("clean_images/" + i)

    #Returns only the "value" of the result
    for i in range(len(result)):
        vals.append(result[i]['value'])

    #Converts those values to a CSV for later use
    convertCSV(vals)


    

if __name__ == "__main__":
    main()
