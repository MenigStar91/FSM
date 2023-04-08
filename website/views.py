from django.shortcuts import render, redirect
import mimetypes
import os
from django.http import HttpResponse   
from django.contrib import messages
import subprocess
from website.models import handle_uploaded_file 

# Create your views here.
def main(request):
    if request.method == 'POST':
        upload = request.FILES['filename'] 
        try:
            handle_uploaded_file(request.FILES['filename'])
            path = "documents/output"  
            fields = tuple(os.listdir(path))  
            return render(request,"main.html", {'dfiles' : fields})  
        except : 
            return HttpResponse("Error")  
    else :
        path = "documents/output"  
        fields = tuple(os.listdir(path))
        return render(request,"main.html", {'dfiles' : fields})  

def download_file(request, filename=''):
    if filename != '':
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '\\documents\\output\\' + filename
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
    else:
        return redirect('')