from django.db import models
import os
import glob
import subprocess  
# Create your models here.

def read_content(f):
    try :
        inputfile = glob.glob(r'documents/input' + '**/*.v')[0]
        os.remove(inputfile)
    except :
        pass

    content = ''
    with open('documents/input/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():  
            destination.write(chunk)  

    for chunk in f.chunks():  
        content += str(chunk, 'UTF-8')
 
    return content 

def handle_uploaded_file():
    runfile()

def upload_cpp_file(f):
    try : 
        cfile = glob.glob(r'documents/generator' + '**/*.cpp')[0]
        os.remove(cfile)
    except :
        pass
   
    with open('documents/generator/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 
   

def delete_prev_data():
    path = "documents/output"  
    ofile = tuple(os.listdir(path))  
    for file in ofile:
        os.remove(path+"/"+file)
        
def runfile():
    subprocess.call(["python", r"documents\generator\verilog.py"])
    
