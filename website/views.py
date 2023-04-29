from django.shortcuts import render, redirect
import mimetypes
import os
import glob
from django.http import HttpResponse   
from django.contrib import messages
import subprocess
from website.models import  *



# Create your views here.
def compile(request):
    cfile = glob.glob(r'documents/input' + '**/*.v')[0]
    with open(cfile) as f:
        content = f.read()

    try:
        handle_uploaded_file()
        path = "documents/output"  
        fields = tuple(os.listdir(path))  
        try : 
            cfile = glob.glob(r'documents/generator' + '**/*.cpp')[0]
        except :
            cfile = ""
        var = 'Compiled Successfully'
        return render(request,"main.html", {'dfiles' : fields, 'cfile' : os.path.basename(cfile), 'console' : var, 'content' : content})  
    except : 
        var = 'Error in compilation'
        return render(request,"main.html", {'dfiles' : fields, 'cfile' : os.path.basename(cfile), 'console' : var, 'content' : content})

def main(request):
    if request.method == 'POST':
        upload = request.FILES['filename']
        if(upload.name.endswith('.v')): 
            try:
                assert(request.FILES['filename'].name.endswith('.v'))
                delete_prev_data()
                content = read_content(request.FILES['filename'])
                path = "documents/output"  
                fields = tuple(os.listdir(path)) 
                try : 
                    cfile = glob.glob(r'documents/generator' + '**/*.cpp')[0]
                except :
                    cfile = ""
                var = 'Verilog file read Successfully'
                return render(request,"main.html", {'dfiles' : fields, 'cfile' : os.path.basename(cfile), 'console' : var, 'content' : content})  
            except : 
                path = "documents/output"  
                fields = tuple(os.listdir(path)) 
                try : 
                    cfile = glob.glob(r'documents/generator' + '**/*.cpp')[0]
                except :
                    cfile = ""
                var = 'Error in compilation'
                content = ''
                return render(request,"main.html", {'dfiles' : fields, 'cfile' : os.path.basename(cfile), 'console' : var, 'content' : content})
                #return HttpResponse("could not upload") 
        elif(upload.name.endswith('.cpp')):
            try:
                assert(request.FILES['filename'].name.endswith('.cpp'))
                delete_prev_data()
                upload_cpp_file(request.FILES['filename'])
                path = "documents/output"  
                fields = tuple(os.listdir(path)) 
                try : 
                    cfile = glob.glob(r'documents/generator' + '**/*.cpp')[0]
                except :
                    cfile = ""
                content = ''
                var = 'Upload your files'
                return render(request,"main.html", {'dfiles' : fields, 'cfile' : os.path.basename(cfile), 'console' : var, 'content' : content})  
            except :
                path = "documents/output"  
                fields = tuple(os.listdir(path)) 
                try : 
                    cfile = glob.glob(r'documents/generator' + '**/*.cpp')[0]
                except :
                    cfile = ""
                var = 'Error in cpp compilation'
                content = ''
                return render(request,"main.html", {'dfiles' : fields, 'cfile' : os.path.basename(cfile), 'console' : var, 'content' : content})
                #return HttpResponse("could not upload") 
        else :
            return HttpResponse("wrong file extension")
    else :
        path = "documents/output"  
        fields = tuple(os.listdir(path))
        try : 
            cfile = glob.glob(r'documents/generator' + '**/*.cpp')[0]
        except :
            cfile = ""
        var = 'Upload your files'
        content = ''
        return render(request,"main.html", {'dfiles' : fields, 'cfile' : os.path.basename(cfile), 'console' : var, 'content':content})  

def download_file(request, filename=''):
    if filename != '':
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if filename.endswith(".cpp"):
            filepath = BASE_DIR + '\\documents\\generator\\' + filename
        else : 
            filepath = BASE_DIR + '\\documents\\output\\' + filename
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
    else:
        return redirect('')