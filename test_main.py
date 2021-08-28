
from fastapi.testclient import TestClient
from main import app
import csv



client = TestClient(app)


def test_upload_file_without_extension():
    # with open("data.csv") as f:
    #     response = client.post("/files", files={"file": ("data.csv", f)})
        # print(f)
    response = client.post(
        "/files", files={'data_file': open('CSV_File/datacsv', 'rb')}
    )
    
    assert response.status_code == 200
    assert response.json() == {
        "status" : "Faild",
        "error_code" : 11,
        'Error' : "Only .CSV file accepted"
    }


def test_upload_file_diff_extension():
    response = client.post(
        "/files", files={'data_file': open('CSV_File/data.txt', 'rb')}
    )
    
    assert response.status_code == 200
    assert response.json() == {
        "status" : "Faild",
        "error_code" : 11,
        'Error' : "Only .CSV file accepted"
    }


def test_upload_csv_file_without_data():
    response = client.post(
        "/files", files={'data_file': open('CSV_File/data_header_only.csv', 'rb')}
    )
    
    assert response.status_code == 200
    assert response.json() == {
        "status" : "Faild",
        "error_code" : 12,
        "Error" : "the uploaded file has no data"
    }



def test_upload_csv_file_with_data():
    response = client.post(
        "/files", files={'data_file': open('CSV_File/data.csv', 'rb')}
    )
    
    assert response.status_code == 200
    assert response.json() == {
        "status": "Success",
        "top_product": "Massoub gift card",
        "product_rating": 5
    }

