from django.shortcuts import render, redirect
import mimetypes
import os
import glob
from django.http import HttpResponse   
from django.contrib import messages
import subprocess
from website.models import  *



# Create your views here.
def main(request):
    if request.method == 'POST':
        upload = request.FILES['filename'] 
        if(upload.name.endswith('.v')): 
            try:
                assert(request.FILES['filename'].name.endswith('.v'))
                delete_prev_data()
                handle_uploaded_file(request.FILES['filename'])
                path = "documents/output"  
                fields = tuple(os.listdir(path))  
                try : 
                    cfile = glob.glob(r'documents/generator' + '**/*.cpp')[0]
                except :
                    cfile = ""
                var = 'Compiled Successfully'
                return render(request,"main.html", {'dfiles' : fields, 'cfile' : os.path.basename(cfile), 'console' : var})  
            except : 
                var = 'Error in compilation'
                return render(request,"main.html", {'dfiles' : fields, 'cfile' : os.path.basename(cfile), 'console' : var})
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
                var = 'Upload your files'
                return render(request,"main.html", {'dfiles' : fields, 'cfile' : os.path.basename(cfile), 'console' : var})  
            except :
                var = 'Error in cpp compilation'
                return render(request,"main.html", {'dfiles' : fields, 'cfile' : os.path.basename(cfile), 'console' : var})
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
        return render(request,"main.html", {'dfiles' : fields, 'cfile' : os.path.basename(cfile), 'console' : var})  

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