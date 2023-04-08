from django.db import models
import os
import subprocess  
# Create your models here.

def handle_uploaded_file(f):
    with open('documents/input/uploadfile.v', 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  
    runfile()

def runfile():
    subprocess.call(["python", r"documents\generator\verilog.py"])
    
