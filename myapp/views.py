from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from myapp.models import *
# Create your views here.
def response(request):
    return HttpResponse("<h1>Welcome to HttpResponse</h1>")


def  html_demo1(request):
    fruits={'fruit_name':["apple","banana","orange","pinapple"]}
    return render(request,"sample.html",context=fruits)


def form_multi_select(request):
    d={}
    if request.method=="POST":
        print(request.POST.getlist("name"))
        d={"signal":True}
        return HttpResponseRedirect(reverse("myapp:response"))
    return render(request,"forms.html",context=d)


def  html_demo2(request):
    d={'data':"Django"}
    return render(request,"sample1.html",context=d)

def display_topics(request):
    data_topic=Webpage.objects.filter(Q(url__startswith="http:") & Q(url__endswith=".com/"))
    # data_webpage=Access_Details.objects.order_by('date')    
    # top={'topics':data_topic,"webpages":data_webpage}
    return render(request,"filter_demo.html",context={'Webpages':data_topic})

def disp_web(request):
    webpages=Webpage.objects.all()
    return render(request,"web.html",context={"webpages":webpages})

def topic_form(request):
    topics=Topic.objects.all()
    if request.method=="POST":
        topic=request.POST.getlist("top")
        webpages=Webpage.objects.none()
        for i in topic:
            webpages=webpages | Webpage.objects.filter(top_name=i)

        return render(request,"web.html",context={"webpages":webpages})
    return render(request,"form_demo.html",context={"topics":topics})

def create_topic(request):
    if request.method=="POST":
        top_name=request.POST.get("top")
        t=Topic.objects.get_or_create(top_name=top_name)[0]
        t.save()
    return render(request,"create_topic.html")

def create_webpage(request):
    if request.method=="POST":
        top_name=request.POST.get("top")
        t=Topic.objects.get_or_create(top_name=top_name)[0]
        t.save()
        name=request.POST.get("name")
        url=request.POST.get("url")
        w=Webpage.objects.get_or_create(top_name=t,name=name,url=url)[0]
        w.save()
    topics=Topic.objects.all()
    return render(request,"create_webpage.html",context={"topics":topics})

def disp_webpage(request):
    webpages=Webpage.objects.all()
    return render(request,"select_name.html",context={"webpages":webpages})

def update_webpage(request):
    if request.method=="POST":
        name=request.POST.get("name")
        webpage=Webpage.objects.get(name=name)
        return render(request,"webpage_update.html",context={"webpage":webpage})
    return HttpResponse("No Data Found")

def up_web(request):
    if request.method=="POST":
        top_name=request.POST.get("top")
        name=request.POST.get("name")
        url=request.POST.get("url")
        t=Topic.objects.get_or_create(top_name=top_name)[0]
        web=Webpage.objects.filter(name=name).update(top_name=t,url=url)
        t.save()
        
    return HttpResponse("<h1>record updated successfully</h1>")