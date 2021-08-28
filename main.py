from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import csv, codecs
from io import StringIO

app = FastAPI()


@app.post("/files")
async def find_max_rate_product(data_file: UploadFile = File(...)):
    file_name =  data_file.filename
    splitFlieNameAndExtension = file_name.split('.')

    # check if filename hasn't an extension 
    # or the extenstion is not csv 
    if len(splitFlieNameAndExtension) <= 1 or splitFlieNameAndExtension[-1].lower() != "csv":
        return {
            "status" : "Faild",
            "error_code" : 11,
            'Error' : "Only .CSV file accepted"
            }


    csv_data = csv.reader(codecs.iterdecode(data_file.file,'utf-8'))
    
    max_average_rate = -1
    max_product_rate = ''
    
    # to skip the header row
    next(csv_data)
    
    # loop rows in csv file
    for id, product, rate in csv_data:
        # convert rate form str to float to be comparable
        rate = float(rate)
        if rate > max_average_rate:
            max_average_rate = rate
            max_product_rate = product
    
    if max_average_rate == -1 and max_product_rate == "": 
        return {
            "status" : "Faild",
            "error_code" : 12,
            "Error" : "the uploaded file has no data"
        }
    

    return {
        "status" : "Success",
        "top_product": max_product_rate,
        "product_rating": max_average_rate
    }

