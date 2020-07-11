#this is my file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def aboutus(request):
    return render(request,'aboutus.html')
def contact(request):
    return render(request,'contact.html')
def navigator(request):
    return render(request,'navigator.html')
def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    if removepunc=='on':
        str1=""
        pun= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in pun:
                str1=str1+char
        param = {"analyzed_text": str1}
        djtext=str1

    if (uppercase=="on"):
        str1 = ""
        for char in djtext:
            char=char.upper()
            str1 = str1 + char
        param = { "analyzed_text": str1}
        djtext=str1


    if (newlineremover=="on"):
        str1 = ""
        for char in djtext:
            if char!="\n" and char!='\r' :
                str1 = str1 + char
        param = {"analyzed_text": str1}
        djtext=str1

    if (spaceremover=="on"):
        str1 = ""
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                str1 = str1 + char
        param = {"analyzed_text": str1}
        djtext=str1

    if (charcount=="on"):
        str1 = str1
        count=0
        for x in djtext:
            count+=1
        str1="total character ="+str(count)+"\r"+str1
        param = {"analyzed_text": str1}

    return render(request, 'analyze.html', param)

    if(removepunc!='on' and uppercase!="on" and newlineremover!="on" and spaceremover!="on" and charcount!="on" ):
        return HttpResponse("error")
