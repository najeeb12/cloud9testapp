from django.shortcuts import render, HttpResponseRedirect, HttpResponse

def home(request):
    return render(request,'testapp/template/home.html')
    
def about(request):
    return render(request,'testapp/template/about.html')