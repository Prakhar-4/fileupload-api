import pyrebase
from fastapi import FastAPI, UploadFile, File
import shutil

app = FastAPI()

# defining firebase configurations
firebaseConfig = {
    "apiKey": "AIzaSyB_sv62PJkq64FQw_iXDTQIipok8d4FluQ",
    "authDomain": "fileupload-69dc5.firebaseapp.com",
    "databaseURL": "gs://fileupload-69dc5.appspot.com",
    "projectId": "fileupload-69dc5",
    "storageBucket": "fileupload-69dc5.appspot.com",
    "messagingSenderId": "3107070695",
    "appId": "1:3107070695:web:da397f04b13c60acb5b842",
    "measurementId": "G-YF11NNV5YV"
}

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()

# POST
@app.post("/upload-file")
async def upload(file: UploadFile = File(...)):
    filetype = file.filename.split('.').pop()
    filename = file.filename[:len(filetype)-1]

    with open(file.filename, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    storage.child(file.filename).put(file.filename)

    return {"filename": file.filename}
