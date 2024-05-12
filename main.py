import os
from shutil import rmtree
from cleanVideos import CleanVideos
from cleanVideoImages import cleanVideoImages
from RunAPI import pentoprint
from convertCSV import convertCSV

#Change the "API_Key" to yours
"1ebe80c4a1mshca1e9f5e61258a1p165b4ejsne2add8a95969"
API_Key= "d040dffd4amsh50eb199d7a58c92p1a7138jsn2ece85c95540"

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