from django.shortcuts import render
from django.http import HttpResponse
from .s3b import getconts, genurl
from .models import UrlConts


# def say_hello(request):
#     return HttpResponse("Hello, Bro!!!")

def home(request):
    lst=getconts()
    arr=[]
    for i in range(len(lst)):
        arr.append([i+1, lst[i]])
    return render(request, "home.html", context={
        "lst":arr,
        "bname":"psh2.svg"
    })

def serve_req(request):
    url=request.POST["inp"]
    x=UrlConts.objects.filter(url=url).values()
    if x.count()>=1:
        arr=[]
        conts=x[0]["conts"]
        conts=conts.split("x0|0x")
        for i in conts:
            arr.append(genurl(i))
        arr=[[i, conts[i], arr[i]] for i in range(len(conts))]
        # UrlConts.objects.filter(url=url).delete()
        return render(request, "ContView.html", context={
            "objs":arr,
            "bname":"psh3.svg"
        })
    return HttpResponse(url)