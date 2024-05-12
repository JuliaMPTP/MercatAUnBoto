import re
import pandas as pd
import datetime

def splitRes(s):
    
    #Divides numbers and strings
    result = re.split("^(.*?)\s+([-+]?\d+(?:[.]\d+)?)\s*(.*)$", s.strip())
    #patron = '([-+]?\d+\.\d+)|([-+]?\d+)' original, it was changed
    resultSplit = [r.strip() for r in result if r is not None and r.strip() != '']

    print(resultSplit)
    # Return None if there are not exactly 3 parts
    
    if len(resultSplit) != 3:
        return None
    
    return resultSplit

def convertCSV(API_RESULT):
    
    date = datetime.date.today()
    finalResult = []
    count = 0

    for i in API_RESULT:
        i = i.replace("'", '.')
        i = i.replace(",", '.')
        i = i.replace("\n", ' ')
        split= splitRes(i)

        if split is not None:
            finalResult.append(split)
        else:
            count += 1
        
    print(finalResult)
    print("There has been", count, "products not detected.")
    
    #Converts the results to a dataframe and later to a CSV
    df = pd.DataFrame(finalResult, columns=['Producto', 'Precio', 'Unidad'])
    df.to_csv("precios_{}.csv".format(date.strftime("%d-%m-%Y")))

    return None



