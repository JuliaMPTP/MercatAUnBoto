import requests
import os


def pentoprint(API_KEY):

    #Folder with the already clean images
    cleanImagesFile = os.listdir('clean_images/')

    result = []

    #For each image in the folder
    for i in cleanImagesFile:

        url = "https://pen-to-print-handwriting-ocr.p.rapidapi.com/recognize/"
        
        files = { "srcImg": open('clean_images/'+ i, 'rb') }
        payload = {
            "includeSubScan": "0",
            "Session": "string"
        }
        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": "pen-to-print-handwriting-ocr.p.rapidapi.com"
        }
        
        response = requests.post(url, data=payload, files=files, headers=headers)
        
        #print(response.json())
        result.append(response.json())

    return result
